# SPL Studio Configuration Manager
# An app module and global plugin package for NVDA
# Copyright 2015-2016 Joseph Lee and others, released under GPL.
# Provides the configuration management package for SPL Studio app module.
# For miscellaneous dialogs and tool, see SPLMisc module.

import os
from cStringIO import StringIO
from configobj import ConfigObj
from validate import Validator
import weakref
import time
import datetime
import cPickle
import globalVars
import ui
import api
import gui
import wx
from winUser import user32
import tones
import splupdate
from splmisc import SPLCountdownTimer

# Configuration management
SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")
SPLProfiles = os.path.join(globalVars.appArgs.configPath, "addons", "stationPlaylist", "profiles")
# New (7.0) style config.
confspec7 = ConfigObj(StringIO("""
[General]
BeepAnnounce = boolean(default=false)
MessageVerbosity = option("beginner", "advanced", default="beginner")
BrailleTimer = option("off", "intro", "outro", "both", default="off")
AlarmAnnounce = option("beep", "message", "both", default="beep")
LibraryScanAnnounce = option("off", "ending", "progress", "numbers", default="off")
TrackDial = boolean(default=false)
CategorySounds = boolean(default=false)
MetadataReminder = option("off", "startup", "instant", default="off")
TimeHourAnnounce = boolean(default=true)
ExploreColumns = string_list(default=list("Artist","Title","Duration","Intro","Category","Filename","Year","Album","Genre","Time Scheduled"))
[IntroOutroAlarms]
SayEndOfTrack = boolean(default=true)
EndOfTrackTime = integer(min=1, max=59, default=5)
SaySongRamp = boolean(default=true)
SongRampTime = integer(min=1, max=9, default=5)
[MicrophoneAlarm]
MicAlarm = integer(min=0, max=7200, default="0")
MicAlarmInterval = integer(min=0, max=60, default=0)
[MetadataStreaming]
MetadataEnabled = bool_list(default=list(false,false,false,false,false))
[ColumnAnnouncement]
UseScreenColumnOrder = boolean(default=true)
ColumnOrder = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
IncludedColumns = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
[SayStatus]
SayScheduledFor = boolean(default=true)
SayListenerCount = boolean(default=true)
SayPlayingCartName = boolean(default=true)
SayPlayingTrackName = string(default="True")
[Advanced]
SPLConPassthrough = boolean(default=false)
CompatibilityLayer = option("off", "jfw", "wineyes", default="off")
ProfileTriggerThreshold = integer(min=5, max=60, default=15)
[Update]
AutoUpdateCheck = boolean(default=true)
[Startup]
AudioDuckingReminder = boolean(default=true)
"""), encoding="UTF-8", list_values=False)
confspec7.newlines = "\r\n"
SPLConfig = None
# A pool of broadcast profiles.
SPLConfigPool = []
# The following settings can be changed in profiles:
_mutatableSettings7=("IntroOutroAlarms", "MicrophoneAlarm", "MetadataStreaming", "ColumnAnnouncement")
# 7.0: Profile-specific confspec (might be removed once a more optimal way to validate sections is found).
# Dictionary comprehension is better here.
confspecprofiles = {sect:key for sect, key in confspec7.iteritems() if sect in _mutatableSettings7}

# Default config spec container.
# To be moved to a different place in 8.0.
_SPLDefaults7 = ConfigObj(None, configspec = confspec7, encoding="UTF-8")
_val = Validator()
_SPLDefaults7.validate(_val, copy=True)

# Display an error dialog when configuration validation fails.
def runConfigErrorDialog(errorText, errorType):
	wx.CallAfter(gui.messageBox, errorText, errorType, wx.OK|wx.ICON_ERROR)

# Reset settings to defaults.
# This will be called when validation fails or when the user asks for it.
# 6.0: The below function resets a single profile. A sister function will reset all of them.
# 7.0: This calls copy profile function with default dictionary as the source profile.
def resetConfig(defaults, activeConfig):
	# The only time everything should be copied is when resetting normal profile.
	copyProfile(defaults, activeConfig, complete=activeConfig.filename == SPLIni)

# Reset all profiles upon request.
def resetAllConfig():
	for profile in SPLConfigPool:
		# Retrieve the profile path, as ConfigObj.reset nullifies it.
		profilePath = profile.filename
		profile.reset()
		profile.filename = profilePath
		# 7.0: Without writing the profile, we end up with inconsistencies between profile cache and actual profile.
		profile.write()
		resetConfig(_SPLDefaults7, profile)
		# Convert certain settings to a different format.
		profile["ColumnAnnouncement"]["IncludedColumns"] = set(_SPLDefaults7["ColumnAnnouncement"]["IncludedColumns"])
	# Translators: A dialog message shown when settings were reset to defaults.
	wx.CallAfter(gui.messageBox, _("Successfully applied default add-on settings."),
	# Translators: Title of the reset config dialog.
	_("Reset configuration"), wx.OK|wx.ICON_INFORMATION)

# In case one or more profiles had config issues, look up the error message from the following map.
_configErrors ={
	"fileReset":"Settings reset to defaults due to configuration file coruption",
	"completeReset":"All settings reset to defaults",
	"partialReset":"Some settings reset to defaults",
	"columnOrderReset":"Column announcement order reset to defaults",
	"partialAndColumnOrderReset":"Some settings, including column announcement order reset to defaults",
	"noInstantProfile":"Cannot find instant profile"
}

# To be run in app module constructor.
# With the load function below, load the config upon request.
# The below init function is really a vehicle that traverses through config profiles in a loop.
# Prompt the config error dialog only once.
_configLoadStatus = {} # Key = filename, value is pass or no pass.

def initConfig():
	# 7.0: When add-on 7.0 starts for the first time, check if a conversion file exists.
	# To be removed in add-on 7.2.
	curInstantProfile = ""
	if os.path.isfile(os.path.join(globalVars.appArgs.configPath, "splstudio7.ini")):
		# Save add-on update related keys and instant profile signature from death.
		# Necessary since the old-style config file contains newer information about update package size, last installed date and records instant profile name.
		tempConfig = ConfigObj(SPLIni)
		if "InstantProfile" in tempConfig: curInstantProfile = tempConfig["InstantProfile"]
		os.remove(SPLIni)
		os.rename(os.path.join(globalVars.appArgs.configPath, "splstudio7.ini"), SPLIni)
	# Load the default config from a list of profiles.
	global SPLConfig, SPLConfigPool, _configLoadStatus, SPLActiveProfile, SPLSwitchProfile
	if SPLConfigPool is None: SPLConfigPool = []
	# Translators: The name of the default (normal) profile.
	if SPLActiveProfile is None: SPLActiveProfile = _("Normal profile")
	SPLConfigPool.append(unlockConfig(SPLIni, profileName=SPLActiveProfile, prefill=True))
	try:
		profiles = filter(lambda fn: os.path.splitext(fn)[-1] == ".ini", os.listdir(SPLProfiles))
		for profile in profiles:
			SPLConfigPool.append(unlockConfig(os.path.join(SPLProfiles, profile), profileName=os.path.splitext(profile)[0]))
	except WindowsError:
		pass
	# Manually set certain options (thankfully, it is cached already, so it'll be saved when the app module dies).
	# To be removed in 7.1.
	SPLConfigPool[0]["General"]["TimeHourAnnounce"] = True
	# 7.0: Store the config as a dictionary.
	# This opens up many possibilities, including config caching, loading specific sections only and others (the latter saves memory).
	SPLConfig = dict(SPLConfigPool[0])
	SPLConfig["ActiveIndex"] = 0 # Holds settings from normal profile.
	if curInstantProfile != "": SPLConfig["InstantProfile"] = curInstantProfile
	# Locate instant profile.
	if "InstantProfile" in SPLConfig:
		try:
			SPLSwitchProfile = SPLConfigPool[getProfileIndexByName(SPLConfig["InstantProfile"])].name
		except ValueError:
			_configLoadStatus[SPLConfigPool[0].name] = "noInstantProfile"
	if len(_configLoadStatus):
		# Translators: Standard error title for configuration error.
		title = _("Studio add-on Configuration error")
		messages = []
		# 6.1: Display just the error message if the only corrupt profile is the normal profile.
		if len(_configLoadStatus) == 1 and SPLActiveProfile in _configLoadStatus:
			# Translators: Error message shown when add-on configuration had issues.
			messages.append("Your add-on configuration had following issues:\n\n")
			messages.append(_configErrors[_configLoadStatus[SPLActiveProfile]])
		else:
			# Translators: Error message shown when add-on configuration had issues.
			messages.append("One or more broadcast profiles had issues:\n\n")
			for profile in _configLoadStatus:
				error = _configErrors[_configLoadStatus[profile]]
				messages.append("{profileName}: {errorMessage}".format(profileName = profile, errorMessage = error))
		_configLoadStatus.clear()
		runConfigErrorDialog("\n".join(messages), title)
	# Fire up profile triggers.
	initProfileTriggers()
	# Let the update check begin.
	splupdate.initialize()

# Unlock (load) profiles from files.
def unlockConfig(path, profileName=None, prefill=False):
	global _configLoadStatus # To be mutated only during unlock routine.
	# Optimization: Profiles other than normal profile contains profile-specific sections only.
	# This speeds up profile loading routine significantly as there is no need to call a function to strip global settings.
	# 7.0: What if profiles have parsing errors?
	# If so, reset everything back to factory defaults.
	try:
		SPLConfigCheckpoint = ConfigObj(path, configspec = confspec7 if prefill else confspecprofiles, encoding="UTF-8")
	except:
		open(path, "w").close()
		SPLConfigCheckpoint = ConfigObj(path, configspec = confspec7 if prefill else confspecprofiles, encoding="UTF-8")
		_configLoadStatus[profileName] = "fileReset"
	# 5.2 and later: check to make sure all values are correct.
	# 7.0: Make sure errors are displayed as config keys are now sections and may need to go through subkeys.
	configTest = SPLConfigCheckpoint.validate(_val, copy=prefill, preserve_errors=True)
	if configTest != True:
		if not configTest:
			# Case 1: restore settings to defaults when 5.x config validation has failed on all values.
			# 6.0: In case this is a user profile, apply base configuration.
			resetConfig(_SPLDefaults7, SPLConfigCheckpoint)
			_configLoadStatus[profileName] = "completeReset"
		elif isinstance(configTest, dict):
			# Case 2: For 5.x and later, attempt to reconstruct the failed values.
			# 6.0: Cherry-pick global settings only.
			# 7.0: Go through failed sections.
			for setting in configTest.keys():
				if isinstance(configTest[setting], dict):
					for failedKey in configTest[setting].keys():
						# 7.0 optimization: just reload from defaults dictionary, as broadcast profiles contain profile-specific settings only.
						SPLConfigCheckpoint[setting][failedKey] = _SPLDefaults7[setting][failedKey]
			# 7.0: Disqualified from being cached this time.
			SPLConfigCheckpoint.write()
			_configLoadStatus[profileName] = "partialReset"
	_extraInitSteps(SPLConfigCheckpoint, profileName=profileName)
	SPLConfigCheckpoint.name = profileName
	# 7.0 optimization: Store an online backup.
	# This online backup is used to prolong SSD life (no need to save a config if it is same as this copy).
	_cacheConfig(SPLConfigCheckpoint)
	return SPLConfigCheckpoint

# Extra initialization steps such as converting value types.
def _extraInitSteps(conf, profileName=None):
	global _configLoadStatus
	columnOrder = conf["ColumnAnnouncement"]["ColumnOrder"]
	# Catch suttle errors.
	fields = _SPLDefaults7["ColumnAnnouncement"]["ColumnOrder"]
	invalidFields = 0
	for field in fields:
		if field not in columnOrder: invalidFields+=1
	if invalidFields or len(columnOrder) != 17:
		if profileName in _configLoadStatus and _configLoadStatus[profileName] == "partialReset":
			_configLoadStatus[profileName] = "partialAndColumnOrderReset"
		else:
			_configLoadStatus[profileName] = "columnOrderReset"
	conf["ColumnAnnouncement"]["ColumnOrder"] = fields
	conf["ColumnAnnouncement"]["IncludedColumns"] = set(conf["ColumnAnnouncement"]["IncludedColumns"])
	# Artist and Title must be present at all times (quite redundant, but just in case).
	conf["ColumnAnnouncement"]["IncludedColumns"].add("Artist")
	conf["ColumnAnnouncement"]["IncludedColumns"].add("Title")
	# Perform a similar check for metadata streaming.
	if len(conf["MetadataStreaming"]["MetadataEnabled"]) != 5:
		if profileName in _configLoadStatus and _configLoadStatus[profileName] == "partialReset":
			_configLoadStatus[profileName] = "partialAndMetadataReset"
		else:
			_configLoadStatus[profileName] = "metadataReset"
		conf["MetadataStreaming"]["MetadataEnabled"] = [False, False, False, False, False]

# Cache a copy of the loaded config.
# This comes in handy when saving configuration to disk. For the most part, no change occurs to config.
# This helps prolong life of a solid-state drive (preventing unnecessary writes).
_SPLCache = {}

def _cacheConfig(conf):
	global _SPLCache
	if _SPLCache is None: _SPLCache = {}
	key = None if conf.filename == SPLIni else conf.name
	_SPLCache[key] = {}
	# Take care of global flags in caching normal profile.
	if "PSZ" in conf:
		_SPLCache[key]["___oldupdatekeys___"] = True
		splupdate.SPLAddonSize = hex(int(conf["PSZ"], 16))
		try: del conf["PSZ"]
		except KeyError: pass
	if "PDT" in conf:
		_SPLCache[key]["___oldupdatekeys___"] = True
		splupdate.SPLAddonCheck = float(conf["PDT"])
		try: del conf["PDT"]
		except KeyError: pass
	for setting in conf.keys():
		if isinstance(conf[setting], dict): _SPLCache[key][setting] = dict(conf[setting])
		else:
			_SPLCache[key][setting] = conf[setting]
			# Optimization: free 5.0-style config keys while the app module is running, to be removed permanently in add-on 7.2.
			if setting != "InstantProfile": del conf[setting]
	# Column inclusion only.
	_SPLCache[key]["ColumnAnnouncement"]["IncludedColumns"] = list(conf["ColumnAnnouncement"]["IncludedColumns"])

# Record profile triggers.
# Each record (profile name) consists of seven fields organized as a list:
# A bit vector specifying which days should this profile be active, the first five fields needed for constructing a datetime.datetime object used to look up when to trigger this profile, and an integer specifying the duration in minutes.
profileTriggers = {} # Using a pickle is quite elegant.
profileTriggers2 = {} # For caching purposes.
# Profile triggers pickle.
SPLTriggersFile = os.path.join(globalVars.appArgs.configPath, "spltriggers.pickle")
# Trigger timer.
triggerTimer = None

# Prepare the triggers dictionary and other runtime support.
def initProfileTriggers():
	global profileTriggers, profileTriggers2, SPLTriggerProfile, triggerTimer
	try:
		profileTriggers = cPickle.load(file(SPLTriggersFile, "r"))
	except IOError:
		profileTriggers = {}
	# Cache profile triggers, used to compare the runtime dictionary against the cache.
	profileTriggers2 = dict(profileTriggers)
	triggerStart()

# Locate time-based profiles if any.
# A 3-tuple will be returned, containing the next trigger time (for time delta calculation), the profile name for this trigger time and whether an immediate switch is necessary.
def nextTimedProfile(current=None):
	if current is None: current = datetime.datetime.now()
	# No need to proceed if no timed profiles are defined.
	if not len(profileTriggers): return None
	possibleTriggers = []
	for profile in profileTriggers.keys():
		shouldBeSwitched = False
		entry = list(profileTriggers[profile])
		# Construct the comparison datetime (see the profile triggers spec).
		triggerTime = datetime.datetime(entry[1], entry[2], entry[3], entry[4], entry[5])
		# Hopefully the trigger should be ready before the show, but sometimes it isn't.
		if current > triggerTime:
			profileTriggers[profile] = setNextTimedProfile(profile, entry[0], datetime.time(entry[4], entry[5]), date=current, duration=entry[6])
			if (current-triggerTime).seconds < entry[6]*60:
				shouldBeSwitched = True
		possibleTriggers.append((triggerTime, profile, shouldBeSwitched))
	return min(possibleTriggers) if len(possibleTriggers) else None

# Some helpers used in locating next air date/time.

# Set the next timed profile.
# Bits indicate the trigger days vector, hhmm is time, with the optional date being a specific date otherwise current date.
def setNextTimedProfile(profile, bits, switchTime, date=None, duration=0):
	if date is None: date = datetime.datetime.now()
	dayIndex = date.weekday()
	triggerCandidate = 64 >> dayIndex
	currentTime = datetime.time(date.hour, date.minute, date.second, date.microsecond)
	# Case 1: Show hasn't begun.
	if (bits & triggerCandidate) and currentTime < switchTime:
		delta = 0
	else:
		# Case 2: This is a weekly show.
		if bits == triggerCandidate:
			delta = 7
		else:
			import math
			# Scan the bit vector until finding the correct date and calculate the resulting delta (dayIndex modulo 7).
			# Take away the current trigger bit as this is invoked once the show air date has passed.
			days = bits-triggerCandidate if bits & triggerCandidate else bits
			currentDay = int(math.log(triggerCandidate, 2))
			nextDay = int(math.log(days, 2))
			# Hoping the resulting vector will have some bits set to 1...
			if triggerCandidate > days:
				delta = currentDay-nextDay
			else:
				triggerBit = -1
				for bit in xrange(currentDay-1, -1, -1):
					if 2 ** bit & days:
						triggerBit = bit
						break
				if triggerBit > -1:
					delta = currentDay-triggerBit
				else:
					delta = 7-(nextDay-currentDay)
	date += datetime.timedelta(delta)
	return [bits, date.year, date.month, date.day, switchTime.hour, switchTime.minute, duration]

# Find if another profile is occupying the specified time slot.
def duplicateExists(map, profile, bits, hour, min, duration):
	if len(map) == 0 or (len(map) == 1 and profile in map): return False
	# Convert hours and minutes to an integer for faster comparison.
	start1 = (hour*60) + min
	end1 = start1+duration
	# A possible duplicate may exist simply because of bits.
	for item in filter(lambda p: p != profile, map.keys()):
		if map[item][0] == bits:
			entry = map[item]
			start2 = (entry[4] * 60) + entry[5]
			end2 = start2+entry[6]
			if start1 <= start2 <= end1 or start2 <= start1 <= end2:
				return True
	return False

# Start the trigger timer based on above information.
# Can be restarted if needed.
def triggerStart(restart=False):
	global SPLTriggerProfile, triggerTimer
	# Restart the timer when called from triggers dialog in order to prevent multiple timers from running.
	if triggerTimer is not None and triggerTimer.IsRunning() and restart:
		triggerTimer.Stop()
		triggerTimer = None
	queuedProfile = nextTimedProfile()
	if queuedProfile is not None:
		try:
			SPLTriggerProfile = queuedProfile[1]
		except ValueError:
			SPLTriggerProfile = None
		# We are in the midst of a show, so switch now.
		if queuedProfile[2]:
			triggerProfileSwitch()
		else:
			switchAfter = (queuedProfile[0] - datetime.datetime.now())
			if switchAfter.days == 0 and switchAfter.seconds <= 3600:
				time.sleep((switchAfter.microseconds+1000) / 1000000.0)
				triggerTimer = SPLCountdownTimer(switchAfter.seconds, triggerProfileSwitch, SPLConfig["Advanced"]["ProfileTriggerThreshold"])
				triggerTimer.Start()

# Dump profile triggers pickle away.
def saveProfileTriggers():
	global triggerTimer, profileTriggers, profileTriggers2
	if triggerTimer is not None and triggerTimer.IsRunning():
		triggerTimer.Stop()
		triggerTimer = None
	# Unless it is a daily show, profile triggers would not have been modified.
	# This trick is employed in order to reduce unnecessary disk writes.
	if profileTriggers != profileTriggers2:
		cPickle.dump(profileTriggers, file(SPLTriggersFile, "wb"))
	profileTriggers = None
	profileTriggers2 = None

# Instant profile switch helpers.
# A number of helper functions assisting instant switch profile routine and others, including sorting and locating the needed profile upon request.

# Fetch the profile index with a given name.
def getProfileIndexByName(name):
	try:
		return [profile.name for profile in SPLConfigPool].index(name)
	except ValueError:
		raise ValueError("The specified profile does not exist")

# And:
def getProfileByName(name):
	return SPLConfigPool[getProfileIndexByName(name)]

# Copy settings across profiles.
# Setting complete flag controls whether profile-specific settings are applied (true otherwise, only set when resetting profiles).
def copyProfile(sourceProfile, targetProfile, complete=False):
	for section in sourceProfile.keys() if complete else _mutatableSettings7:
		targetProfile[section] = dict(sourceProfile[section])

# Merge sections when switching profiles.
# This is also employed by the routine which saves changes to a profile when user selects a different profile from add-on settings dialog.
# Profiles refer to indecies.
# Active refers to whether this is a runtime switch (false if saving profiles).
def mergeSections(profile, active=True):
	global SPLConfig, SPLConfigPool
	copyProfile(SPLConfigPool[profile], SPLConfig)
	if active: SPLConfig["ActiveIndex"] = profile

# A reverse of the above.
def applySections(profile, key=None):
	global SPLConfig, SPLConfigPool
	if key is None:
		copyProfile(SPLConfig, SPLConfigPool[profile])
	else:
		# A slash (/) will denote section/key hierarchy.
		tree, leaf = key.split("/")
		if tree in SPLConfig:
			if leaf == "": # Section only.
				SPLConfigPool[profile][tree] = dict(SPLConfig[tree])
			else:
				SPLConfigPool[profile][tree][leaf] = SPLConfig[tree][leaf]

# Last but not least...
# Module level version of get profile flags function.
# Optional keyword arguments are to be added when called from dialogs such as add-on settings.
# A crucial kwarg is contained, and if so, profile flags set will be returned.
def getProfileFlags(name, active=None, instant=None, triggers=None, contained=False):
	flags = set()
	if active is None: active = SPLActiveProfile
	if instant is None: instant = SPLSwitchProfile
	if triggers is None: triggers = profileTriggers
	if name == active:
		# Translators: A flag indicating the currently active broadcast profile.
		flags.add(_("active"))
	if name == instant:
		# Translators: A flag indicating the broadcast profile is an instant switch profile.
		flags.add(_("instant switch"))
	if name in triggers:
		# Translators: A flag indicating the time-based triggers profile.
		flags.add(_("time-based"))
	if not contained:
		return name if len(flags) == 0 else "{0} <{1}>".format(name, ", ".join(flags))
	else: return flags

# Is the config pool itself sorted?
# This check is performed when displaying broadcast profiles.
def isConfigPoolSorted():
		profileNames = [profile.name for profile in SPLConfigPool][1:]
		for pos in xrange(len(profileNames)-1):
			if profileNames[pos] > profileNames[pos+1]:
				return False
		return True


# Perform some extra work before writing the config file.
def _preSave(conf):
	# Perform global setting processing only for the normal profile.
	# 7.0: if this is a second pass, index 0 may not be normal profile at all.
	# Use profile path instead.
	if conf.filename == SPLIni:
		# Cache instant profile for later use.
		if SPLSwitchProfile is not None:
			conf["InstantProfile"] = SPLSwitchProfile
			# 7.0: Also update the runtime dictionary.
			SPLConfig["InstantProfile"] = SPLSwitchProfile
		else:
			try:
				del conf["InstantProfile"]
			except KeyError:
				pass
		# Todo for 7.2: Remove obsolete keys from normal profile (not runtime config yet).
		# Del PlaylistRemainder.
	# For other profiles, remove global settings before writing to disk.
	else:
		# 6.1: Make sure column inclusion aren't same as default values.
		if len(conf["ColumnAnnouncement"]["IncludedColumns"]) == 17:
			del conf["ColumnAnnouncement"]["IncludedColumns"]
		for setting in conf.keys():
			for key in conf[setting].keys():
				try:
					if conf[setting][key] == _SPLDefaults7[setting][key]:
						del conf[setting][key]
				except KeyError:
					pass
			if setting in conf and not len(conf[setting]):
				del conf[setting]

# Check if the profile should be written to disk.
# For the most part, no setting will be modified.
def shouldSave(profile):
	tree = None if profile.filename == SPLIni else profile.name
	# One downside of caching: new profiles are not recognized as such.
	if "___new___" in _SPLCache[tree]: return True
	# Playlist Remainder, be gone!
	if "Advanced" in profile and "PlaylistRemainder" in profile["Advanced"]:
		del profile["Advanced"]["PlaylistRemainder"]
		return True
	# Goodbye old-style update keys (to be removed in add-on 7.1).
	if "___oldupdatekeys___" in _SPLCache[tree]: return True
	for section in profile.keys():
		if isinstance(profile[section], dict):
			for key in profile[section]:
				if profile[section][key] != _SPLCache[tree][section][key]:
					return True # Setting modified.
	return False


# Save configuration database.
def saveConfig():
	# Save all config profiles.
	global SPLConfig, SPLConfigPool, SPLActiveProfile, SPLPrevProfile, SPLSwitchProfile, _SPLCache
	# 7.0: Turn off auto update check timer.
	if splupdate._SPLUpdateT is not None and splupdate._SPLUpdateT.IsRunning(): splupdate._SPLUpdateT.Stop()
	splupdate._SPLUpdateT = None
	# Close profile triggers dictionary.
	saveProfileTriggers()
	# Save update check state.
	splupdate.terminate()
	# Save profile-specific settings to appropriate dictionary if this is the case.
	activeIndex = SPLConfig["ActiveIndex"]
	del SPLConfig["ActiveIndex"]
	if activeIndex > 0:
		applySections(activeIndex)
	# 7.0: Save normal profile first.
	# Temporarily merge normal profile.
	mergeSections(0)
	# 6.1: Transform column inclusion data structure (for normal profile) now.
	# 7.0: This will be repeated for broadcast profiles later.
	SPLConfigPool[0]["ColumnAnnouncement"]["IncludedColumns"] = list(SPLConfigPool[0]["ColumnAnnouncement"]["IncludedColumns"])
	_preSave(SPLConfigPool[0])
	# Global flags, be gone.
	del SPLConfig["ColumnExpRange"]
	# Convert keys back to 5.x format.
	for section in SPLConfigPool[0].keys():
		if isinstance(SPLConfigPool[0][section], dict):
			for key in SPLConfigPool[0][section]:
				SPLConfigPool[0][key] = SPLConfigPool[0][section][key]
	# Disk write optimization check please.
	if shouldSave(SPLConfigPool[0]):
		SPLConfigPool[0].write()
	del SPLConfigPool[0]
	# Now save broadcast profiles.
	for configuration in SPLConfigPool:
		if configuration is not None:
			configuration["ColumnAnnouncement"]["IncludedColumns"] = list(configuration["ColumnAnnouncement"]["IncludedColumns"])
			# 7.0: See if profiles themselves must be saved.
			# This must be done now, otherwise changes to broadcast profiles (cached) will not be saved as presave removes them.
			if shouldSave(configuration):
				_preSave(configuration)
				# 7.0: Convert profile-specific settings back to 5.x format in case add-on 6.x will be installed later (not recommended).
				# This will be removed in add-on 7.2.
				if len(configuration) > 0:
					for section in configuration.keys():
						if isinstance(configuration[section], dict):
							for key in configuration[section]:
								configuration[key] = configuration[section][key]
				configuration.write()
	SPLConfig.clear()
	SPLConfig = None
	SPLConfigPool = None
	SPLActiveProfile = None
	SPLPrevProfile = None
	SPLSwitchProfile = None
	_SPLCache.clear()
	_SPLCache = None


# Switch between profiles.
SPLActiveProfile = None
SPLPrevProfile = None
SPLSwitchProfile = None
SPLTriggerProfile = None

# A general-purpose profile switcher.
# Allows the add-on to switch between profiles as a result of manual intervention or through profile trigger timer.
# Instant profile switching is just a special case of this function.
def switchProfile(activeProfile, newProfile):
	global SPLConfig, SPLActiveProfile
	mergeSections(newProfile)
	SPLActiveProfile = SPLConfigPool[newProfile].name
	SPLConfig["ActiveIndex"] = newProfile
	# Use the focus.appModule's metadata reminder method if told to do so now.
	if SPLConfig["General"]["MetadataReminder"] in ("startup", "instant"):
		api.getFocusObject().appModule._metadataAnnouncer(reminder=True)

# Called from within the app module.
def instantProfileSwitch():
	global SPLPrevProfile, SPLConfig, SPLActiveProfile
	if _configDialogOpened:
		# Translators: Presented when trying to switch to an instant switch profile when add-on settings dialog is active.
		ui.message(_("Add-on settings dialog is open, cannot switch profiles"))
		return
	if SPLSwitchProfile is None:
		# Translators: Presented when trying to switch to an instant switch profile when the instant switch profile is not defined.
		ui.message(_("No instant switch profile is defined"))
	else:
		if SPLPrevProfile is None:
			if SPLActiveProfile == SPLSwitchProfile:
				# Translators: Presented when trying to switch to an instant switch profile when one is already using the instant switch profile.
				ui.message(_("You are already in the instant switch profile"))
				return
			# Switch to the given profile.
			switchProfileIndex = getProfileIndexByName(SPLSwitchProfile)
			# 6.1: Do to referencing nature of Python, use the profile index function to locate the index for the soon to be deactivated profile.
			SPLPrevProfile = getProfileIndexByName(SPLActiveProfile)
			# Pass in the prev profile, which will be None for instant profile switch.
			switchProfile(SPLPrevProfile, switchProfileIndex)
			# Translators: Presented when switch to instant switch profile was successful.
			ui.message(_("Switching profiles"))
			# Pause automatic update checking.
			if SPLConfig["Update"]["AutoUpdateCheck"]:
				if splupdate._SPLUpdateT is not None and splupdate._SPLUpdateT.IsRunning: splupdate._SPLUpdateT.Stop()
		else:
			switchProfile(None, SPLPrevProfile)
			SPLPrevProfile = None
			# Translators: Presented when switching from instant switch profile to a previous profile.
			ui.message(_("Returning to previous profile"))
			# Resume auto update checker if told to do so.
			if SPLConfig["Update"]["AutoUpdateCheck"]: updateInit()

# The triggers version of the above function.
# 7.0: Try consolidating this into one or some more functions.
_SPLTriggerEndTimer = None
# Record if time-based profile is active or not.
_triggerProfileActive = False

def triggerProfileSwitch():
	global SPLPrevProfile, SPLConfig, SPLActiveProfile, triggerTimer, _SPLTriggerEndTimer, _triggerProfileActive
	if _configDialogOpened:
		# Translators: Presented when trying to switch profiles when add-on settings dialog is active.
		ui.message(_("Add-on settings dialog is open, cannot switch profiles"))
		return
	if SPLTriggerProfile is None:
		# Technically a dead code, but for now...
		# Translators: Presented when trying to switch to an instant switch profile when the instant switch profile is not defined.
		ui.message(_("No profile triggers defined"))
	else:
		if SPLPrevProfile is None:
			if SPLActiveProfile == SPLTriggerProfile:
				# Translators: Presented when trying to switch to an instant switch profile when one is already using the instant switch profile.
				ui.message(_("A profile trigger is already active"))
				return
			# Switch to the given profile.
			triggerProfileIndex = getProfileIndexByName(SPLTriggerProfile)
			SPLPrevProfile = getProfileIndexByName(SPLActiveProfile)
			# Pass in the prev profile, which will be None for instant profile switch.
			switchProfile(SPLPrevProfile, triggerProfileIndex)
			# Set the global trigger flag to inform various subsystems such as add-on settings dialog.
			_triggerProfileActive = True
			# Translators: Presented when switch to instant switch profile was successful.
			ui.message(_("Switching profiles"))
			# Pause automatic update checking.
			if SPLConfig["Update"]["AutoUpdateCheck"]:
				if splupdate._SPLUpdateT is not None and splupdate._SPLUpdateT.IsRunning: splupdate._SPLUpdateT.Stop()
			# Set the next trigger date and time.
			triggerSettings = profileTriggers[SPLTriggerProfile]
			# Set next trigger if no duration is specified.
			if triggerSettings[6] == 0:
				profileTriggers[SPLTriggerProfile] = setNextTimedProfile(SPLTriggerProfile, triggerSettings[0], datetime.time(triggerSettings[4], triggerSettings[5]))
			else:
				_SPLTriggerEndTimer = wx.PyTimer(triggerProfileSwitch)
				_SPLTriggerEndTimer.Start(triggerSettings[6] * 60 * 1000, True)
		else:
			switchProfile(None, SPLPrevProfile)
			_triggerProfileActive = False
			SPLPrevProfile = None
			# Translators: Presented when switching from instant switch profile to a previous profile.
			ui.message(_("Returning to previous profile"))
			# Resume auto update checker if told to do so.
			if SPLConfig["Update"]["AutoUpdateCheck"]: updateInit()
			# Stop the ending timer.
			if _SPLTriggerEndTimer is not None and _SPLTriggerEndTimer.IsRunning():
				_SPLTriggerEndTimer.Stop()
				_SPLTriggerEndTimer = None


# Automatic update checker.

# The function below is called as part of the update check timer.
# Its only job is to call the update check function (splupdate) with the auto check enabled.
# The update checker will not be engaged if an instant switch profile is active or it is not time to check for it yet (check will be done every 24 hours).
def autoUpdateCheck():
	ui.message("Checking for add-on updates...")
	splupdate.updateCheck(auto=True, continuous=SPLConfig["Update"]["AutoUpdateCheck"])

# The timer itself.
# A bit simpler than NVDA Core's auto update checker.
def updateInit():
	currentTime = time.time()
	nextCheck = splupdate.SPLAddonCheck+86400.0
	if splupdate.SPLAddonCheck < currentTime < nextCheck:
		interval = int(nextCheck - currentTime)
	elif splupdate.SPLAddonCheck < nextCheck < currentTime:
		interval = 86400
		# Call the update check now.
		splupdate.updateCheck(auto=True) # No repeat here.
	splupdate._SPLUpdateT = wx.PyTimer(autoUpdateCheck)
	splupdate._SPLUpdateT.Start(interval * 1000, True)


# Let SPL track item know if it needs to build descriptoin pieces.
# To be renamed and used in other places in 7.0.
def _shouldBuildDescriptionPieces():
	return (not SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"]
	and (SPLConfig["ColumnAnnouncement"]["ColumnOrder"] != _SPLDefaults7["ColumnAnnouncement"]["ColumnOrder"]
	or len(SPLConfig["ColumnAnnouncement"]["IncludedColumns"]) != 17))


# Configuration dialog.
_configDialogOpened = False

class SPLConfigDialog(gui.SettingsDialog):
	# Translators: This is the label for the StationPlaylist Studio configuration dialog.
	title = _("Studio Add-on Settings")

	def makeSettings(self, settingsSizer):

		# Broadcast profile controls were inspired by Config Profiles dialog in NVDA Core.
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select a broadcast profile.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Broadcast &profile:"))
		# Sort profiles for display purposes (the config pool might not be sorted).
		sortedProfiles = [profile.name for profile in SPLConfigPool]
		# No need to sort if the only living profile is the normal configuration or there is one other profile besides this.
		# Optimization: Only sort if config pool itself isn't  - usually after creating, renaming or deleting profile(s).
		if len(sortedProfiles) > 2 and not isConfigPoolSorted():
			firstProfile = SPLConfigPool[0].name
			sortedProfiles = [firstProfile] + sorted(sortedProfiles[1:])
		# 7.0: Have a copy of the sorted profiles so the actual combo box items can show profile flags.
		self.profileNames = list(sortedProfiles)
		self.profiles = wx.Choice(self, wx.ID_ANY, choices=self.displayProfiles(sortedProfiles))
		self.profiles.Bind(wx.EVT_CHOICE, self.onProfileSelection)
		try:
			self.profiles.SetSelection(self.profileNames.index(SPLActiveProfile))
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.profiles)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Profile controls code credit: NV Access (except copy button).
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label of a button to create a new broadcast profile.
		item = newButton = wx.Button(self, label=_("&New"))
		item.Bind(wx.EVT_BUTTON, self.onNew)
		sizer.Add(item)
		# Translators: The label of a button to copy a broadcast profile.
		item = copyButton = wx.Button(self, label=_("Cop&y"))
		item.Bind(wx.EVT_BUTTON, self.onCopy)
		sizer.Add(item)
		# Translators: The label of a button to rename a broadcast profile.
		item = self.renameButton = wx.Button(self, label=_("&Rename"))
		item.Bind(wx.EVT_BUTTON, self.onRename)
		sizer.Add(item)
		# Translators: The label of a button to delete a broadcast profile.
		item = self.deleteButton = wx.Button(self, label=_("&Delete"))
		item.Bind(wx.EVT_BUTTON, self.onDelete)
		sizer.Add(item)
		# Have a copy of the triggers dictionary.
		self._profileTriggersConfig = dict(profileTriggers)
		# Translators: The label of a button to manage show profile triggers.
		item = self.triggerButton = wx.Button(self, label=_("&Triggers..."))
		item.Bind(wx.EVT_BUTTON, self.onTriggers)
		sizer.Add(item)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.switchProfile = SPLSwitchProfile
		self.activeProfile = SPLActiveProfile
		# Used as sanity check in case switch profile is renamed or deleted.
		self.switchProfileRenamed = False
		self.switchProfileDeleted = False
		# Translators: The label for a setting in SPL Add-on settings to configure countdown seconds before switching profiles.
		self.triggerThresholdLabel = wx.StaticText(self, wx.ID_ANY, label=_("Countdown seconds before switching profiles"))
		sizer.Add(self.triggerThresholdLabel)
		self.triggerThreshold = wx.SpinCtrl(self, wx.ID_ANY, min=10, max=60)
		self.triggerThreshold.SetValue(long(SPLConfig["Advanced"]["ProfileTriggerThreshold"]))
		self.triggerThreshold.SetSelection(-1, -1)
		sizer.Add(self.triggerThreshold)
		if SPLConfig["ActiveIndex"] == 0:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.triggerButton.Disable()
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to set status announcement between words and beeps.
		self.beepAnnounceCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Beep for status announcements"))
		self.beepAnnounceCheckbox.SetValue(SPLConfig["General"]["BeepAnnounce"])
		settingsSizer.Add(self.beepAnnounceCheckbox, border=10,flag=wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to set message verbosity.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Message &verbosity:"))
		# Translators: One of the message verbosity levels.
		self.verbosityLevels=[("beginner",_("beginner")),
		# Translators: One of the message verbosity levels.
		("advanced",_("advanced"))]
		self.verbosityList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.verbosityLevels])
		currentVerbosity=SPLConfig["General"]["MessageVerbosity"]
		selection = (x for x,y in enumerate(self.verbosityLevels) if y[0]==currentVerbosity).next()  
		try:
			self.verbosityList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.verbosityList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		self.outroSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Check box hiding method comes from Alberto Buffolino's Columns Review add-on.
		# Translators: Label for a check box in SPL add-on settings to notify when end of track (outro) is approaching.
		self.outroCheckBox=wx.CheckBox(self,wx.NewId(),label=_("&Notify when end of track is approaching"))
		self.outroCheckBox.SetValue(SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"])
		self.outroCheckBox.Bind(wx.EVT_CHECKBOX, self.onOutroCheck)
		self.outroSizer.Add(self.outroCheckBox, border=10,flag=wx.BOTTOM)

		# Translators: The label for a setting in SPL Add-on settings to specify end of track (outro) alarm.
		self.outroAlarmLabel = wx.StaticText(self, wx.ID_ANY, label=_("&End of track alarm in seconds"))
		self.outroSizer.Add(self.outroAlarmLabel)
		self.endOfTrackAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=1, max=59)
		self.endOfTrackAlarm.SetValue(long(SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"]))
		self.endOfTrackAlarm.SetSelection(-1, -1)
		self.outroSizer.Add(self.endOfTrackAlarm)
		self.onOutroCheck(None)
		settingsSizer.Add(self.outroSizer, border=10, flag=wx.BOTTOM)

		self.introSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: Label for a check box in SPL add-on settings to notify when end of intro is approaching.
		self.introCheckBox=wx.CheckBox(self,wx.NewId(),label=_("&Notify when end of introduction is approaching"))
		self.introCheckBox.SetValue(SPLConfig["IntroOutroAlarms"]["SaySongRamp"])
		self.introCheckBox.Bind(wx.EVT_CHECKBOX, self.onIntroCheck)
		self.introSizer.Add(self.introCheckBox, border=10,flag=wx.BOTTOM)

		# Translators: The label for a setting in SPL Add-on settings to specify track intro alarm.
		self.introAlarmLabel = wx.StaticText(self, wx.ID_ANY, label=_("&Track intro alarm in seconds"))
		self.introSizer.Add(self.introAlarmLabel)
		self.songRampAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=1, max=9)
		self.songRampAlarm.SetValue(long(SPLConfig["IntroOutroAlarms"]["SongRampTime"]))
		self.songRampAlarm.SetSelection(-1, -1)
		self.introSizer.Add(self.songRampAlarm)
		self.onIntroCheck(None)
		settingsSizer.Add(self.introSizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control braille timer.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Braille timer:"))
		self.brailleTimerValues=[("off",_("Off")),
		# Translators: One of the braille timer settings.
		("outro",_("Track ending")),
		# Translators: One of the braille timer settings.
		("intro",_("Track intro")),
		# Translators: One of the braille timer settings.
		("both",_("Track intro and ending"))]
		self.brailleTimerList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.brailleTimerValues])
		brailleTimerCurValue=SPLConfig["General"]["BrailleTimer"]
		selection = (x for x,y in enumerate(self.brailleTimerValues) if y[0]==brailleTimerCurValue).next()  
		try:
			self.brailleTimerList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.brailleTimerList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		self.micSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL Add-on settings to change microphone alarm setting.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Microphone alarm in seconds"))
		self.micSizer.Add(label)
		self.micAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=7200)
		self.micAlarm.SetValue(long(SPLConfig["MicrophoneAlarm"]["MicAlarm"]))
		self.micAlarm.SetSelection(-1, -1)
		self.micSizer.Add(self.micAlarm)

		# Translators: The label for a setting in SPL Add-on settings to specify mic alarm interval.
		self.micAlarmIntervalLabel = wx.StaticText(self, wx.ID_ANY, label=_("Microphone alarm &interval in seconds"))
		self.micSizer.Add(self.micAlarmIntervalLabel)
		self.micAlarmInterval = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=60)
		self.micAlarmInterval.SetValue(long(SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"]))
		self.micAlarmInterval.SetSelection(-1, -1)
		self.micSizer.Add(self.micAlarmInterval)
		settingsSizer.Add(self.micSizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control alarm announcement type.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Alarm notification:"))
		# Translators: One of the alarm notification options.
		self.alarmAnnounceValues=[("beep",_("beep")),
		# Translators: One of the alarm notification options.
		("message",_("message")),
		# Translators: One of the alarm notification options.
		("both",_("both beep and message"))]
		self.alarmAnnounceList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.alarmAnnounceValues])
		alarmAnnounceCurValue=SPLConfig["General"]["AlarmAnnounce"]
		selection = (x for x,y in enumerate(self.alarmAnnounceValues) if y[0]==alarmAnnounceCurValue).next()  
		try:
			self.alarmAnnounceList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.alarmAnnounceList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control library scan announcement.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Library scan announcement:"))
		self.libScanValues=[("off",_("Off")),
		# Translators: One of the library scan announcement settings.
		("ending",_("Start and end only")),
		# Translators: One of the library scan announcement settings.
		("progress",_("Scan progress")),
		# Translators: One of the library scan announcement settings.
		("numbers",_("Scan count"))]
		self.libScanList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.libScanValues])
		libScanCurValue=SPLConfig["General"]["LibraryScanAnnounce"]
		selection = (x for x,y in enumerate(self.libScanValues) if y[0]==libScanCurValue).next()  
		try:
			self.libScanList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.libScanList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce time including hours.
		self.hourAnnounceCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Include &hours when announcing track or playlist duration"))
		self.hourAnnounceCheckbox.SetValue(SPLConfig["General"]["TimeHourAnnounce"])
		settingsSizer.Add(self.hourAnnounceCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle track dial mode on and off.
		self.trackDialCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Track Dial mode"))
		self.trackDialCheckbox.SetValue(SPLConfig["General"]["TrackDial"])
		settingsSizer.Add(self.trackDialCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle category sound announcement.
		self.categorySoundsCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Beep for different track categories"))
		self.categorySoundsCheckbox.SetValue(SPLConfig["General"]["CategorySounds"])
		settingsSizer.Add(self.categorySoundsCheckbox, border=10,flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to be notified that metadata streaming is enabled.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Metadata streaming notification and connection"))
		self.metadataValues=[("off",_("Off")),
		# Translators: One of the metadata notification settings.
		("startup",_("When Studio starts")),
		# Translators: One of the metadata notification settings.
		("instant",_("When instant switch profile is active"))]
		self.metadataList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.metadataValues])
		metadataCurValue=SPLConfig["General"]["MetadataReminder"]
		selection = (x for x,y in enumerate(self.metadataValues) if y[0]==metadataCurValue).next()  
		try:
			self.metadataList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.metadataList)
		self.metadataStreams = list(SPLConfig["MetadataStreaming"]["MetadataEnabled"])
		# Translators: The label of a button to manage column announcements.
		item = manageMetadataButton = wx.Button(self, label=_("Configure metadata &streaming connection options..."))
		item.Bind(wx.EVT_BUTTON, self.onManageMetadata)
		sizer.Add(item)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle custom column announcement.
		self.columnOrderCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce columns in the &order shown on screen"))
		self.columnOrderCheckbox.SetValue(SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"])
		self.columnOrder = SPLConfig["ColumnAnnouncement"]["ColumnOrder"]
		# Without manual conversion below, it produces a rare bug where clicking cancel after changing column inclusion causes new set to be retained.
		self.includedColumns = set(SPLConfig["ColumnAnnouncement"]["IncludedColumns"])
		settingsSizer.Add(self.columnOrderCheckbox, border=10,flag=wx.BOTTOM)
		# Translators: The label of a button to manage column announcements.
		item = manageColumnsButton = wx.Button(self, label=_("&Manage track column announcements..."))
		item.Bind(wx.EVT_BUTTON, self.onManageColumns)
		settingsSizer.Add(item)
		# Translators: The label of a button to configure columns explorer slots (SPL Assistant, number row keys to announce specific columns).
		item = columnsExplorerButton = wx.Button(self, label=_("Columns E&xplorer..."))
		item.Bind(wx.EVT_BUTTON, self.onColumnsExplorer)
		self.exploreColumns = SPLConfig["General"]["ExploreColumns"]
		settingsSizer.Add(item)

		# Say status flags to be picked up by the dialog of this name.
		self.scheduledFor = SPLConfig["SayStatus"]["SayScheduledFor"]
		self.listenerCount = SPLConfig["SayStatus"]["SayListenerCount"]
		self.cartName = SPLConfig["SayStatus"]["SayPlayingCartName"]
		self.playingTrackName = SPLConfig["SayStatus"]["SayPlayingTrackName"]

		# Translators: The label of a button to open advanced options such as using SPL Controller command to invoke Assistant layer.
		item = sayStatusButton = wx.Button(self, label=_("&Status announcements..."))
		item.Bind(wx.EVT_BUTTON, self.onStatusAnnouncement)
		settingsSizer.Add(item)

		# Translators: The label of a button to open advanced options such as using SPL Controller command to invoke Assistant layer.
		item = advancedOptButton = wx.Button(self, label=_("&Advanced options..."))
		item.Bind(wx.EVT_BUTTON, self.onAdvancedOptions)
		self.splConPassthrough = SPLConfig["Advanced"]["SPLConPassthrough"]
		self.compLayer = SPLConfig["Advanced"]["CompatibilityLayer"]
		self.autoUpdateCheck = SPLConfig["Update"]["AutoUpdateCheck"]
		settingsSizer.Add(item)

		# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		self.resetConfigButton = wx.Button(self, wx.ID_ANY, label=_("Reset settings"))
		self.resetConfigButton.Bind(wx.EVT_BUTTON,self.onResetConfig)
		settingsSizer.Add(self.resetConfigButton)

	def postInit(self):
		global _configDialogOpened
		_configDialogOpened = True
		self.profiles.SetFocus()

	def onOk(self, evt):
		global SPLConfig, SPLActiveProfile, _configDialogOpened, SPLSwitchProfile, SPLPrevProfile, profileTriggers, _triggerProfileActive
		selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
		profileIndex = getProfileIndexByName(selectedProfile)
		SPLConfig["General"]["BeepAnnounce"] = self.beepAnnounceCheckbox.Value
		SPLConfig["General"]["MessageVerbosity"] = self.verbosityLevels[self.verbosityList.GetSelection()][0]
		SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"] = self.outroCheckBox.Value
		SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"] = self.endOfTrackAlarm.Value
		SPLConfig["IntroOutroAlarms"]["SaySongRamp"] = self.introCheckBox.Value
		SPLConfig["IntroOutroAlarms"]["SongRampTime"] = self.songRampAlarm.Value
		SPLConfig["General"]["BrailleTimer"] = self.brailleTimerValues[self.brailleTimerList.GetSelection()][0]
		SPLConfig["MicrophoneAlarm"]["MicAlarm"] = self.micAlarm.Value
		SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] = self.micAlarmInterval.Value
		SPLConfig["General"]["AlarmAnnounce"] = self.alarmAnnounceValues[self.alarmAnnounceList.GetSelection()][0]
		SPLConfig["General"]["LibraryScanAnnounce"] = self.libScanValues[self.libScanList.GetSelection()][0]
		SPLConfig["General"]["TimeHourAnnounce"] = self.hourAnnounceCheckbox.Value
		SPLConfig["General"]["TrackDial"] = self.trackDialCheckbox.Value
		SPLConfig["General"]["CategorySounds"] = self.categorySoundsCheckbox.Value
		SPLConfig["General"]["MetadataReminder"] = self.metadataValues[self.metadataList.GetSelection()][0]
		SPLConfig["MetadataStreaming"]["MetadataEnabled"] = self.metadataStreams
		SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"] = self.columnOrderCheckbox.Value
		SPLConfig["ColumnAnnouncement"]["ColumnOrder"] = self.columnOrder
		SPLConfig["ColumnAnnouncement"]["IncludedColumns"] = self.includedColumns
		SPLConfig["General"]["ExploreColumns"] = self.exploreColumns
		SPLConfig["SayStatus"]["SayScheduledFor"] = self.scheduledFor
		SPLConfig["SayStatus"]["SayListenerCount"] = self.listenerCount
		SPLConfig["SayStatus"]["SayPlayingCartName"] = self.cartName
		SPLConfig["SayStatus"]["SayPlayingTrackName"] = self.playingTrackName
		SPLConfig["Advanced"]["SPLConPassthrough"] = self.splConPassthrough
		SPLConfig["Advanced"]["CompatibilityLayer"] = self.compLayer
		SPLConfig["Update"]["AutoUpdateCheck"] = self.autoUpdateCheck
		SPLConfig["ActiveIndex"] = profileIndex
		# Reverse of merge: save profile specific sections to individual config dictionaries.
		applySections(profileIndex)
		SPLActiveProfile = selectedProfile
		SPLSwitchProfile = self.switchProfile
		# Make sure to nullify prev profile if instant switch profile is gone.
		# 7.0: Don't do the following in the midst of a broadcast.
		if self.switchProfile is None and not _triggerProfileActive:
			SPLPrevProfile = None
		_configDialogOpened = False
		# 7.0: Perform extra action such as restarting auto update timer.
		self.onCloseExtraAction()
		# Apply changes to profile triggers.
		profileTriggers = dict(self._profileTriggersConfig)
		self._profileTriggersConfig.clear()
		self._profileTriggersConfig = None
		triggerStart(restart=True)
		super(SPLConfigDialog,  self).onOk(evt)

	def onCancel(self, evt):
		global _configDialogOpened, SPLActiveProfile, SPLSwitchProfile, SPLConfig, profileTriggers
		# 6.1: Discard changes to included columns set.
		self.includedColumns.clear()
		self.includedColumns = None
		# Apply profile trigger changes if any.
		profileTriggers = dict(self._profileTriggersConfig)
		self._profileTriggersConfig.clear()
		self._profileTriggersConfig = None
		triggerStart(restart=True)
		# 7.0: No matter what happens, merge appropriate profile.
		try:
			prevActive = self.profileNames.index(self.activeProfile)
		except ValueError:
			prevActive = 0
		mergeSections(prevActive)
		if self.switchProfileRenamed or self.switchProfileDeleted:
			SPLSwitchProfile = self.switchProfile
		if self.switchProfileDeleted:
			SPLActiveProfile = SPLConfigPool[prevActive].name
		_configDialogOpened = False
		super(SPLConfigDialog,  self).onCancel(evt)

	# Perform extra action when closing this dialog such as restarting update timer.
	def onCloseExtraAction(self):
		# Change metadata streaming.
		hwnd = user32.FindWindowA("SPLStudio", None)
		if hwnd:
			for url in xrange(5):
				dataLo = 0x00010000 if SPLConfig["MetadataStreaming"]["MetadataEnabled"][url] else 0xffff0000
				user32.SendMessageW(hwnd, 1024, dataLo | url, 36)
		# Coordinate auto update timer restart routine if told to do so.
		if not SPLConfig["Update"]["AutoUpdateCheck"]:
			if splupdate._SPLUpdateT is not None and splupdate._SPLUpdateT.IsRunning(): splupdate._SPLUpdateT.Stop()
			splupdate._SPLUpdateT = None
		else:
			if splupdate._SPLUpdateT is None: updateInit()

	# Check events for outro and intro alarms, respectively.
	def onOutroCheck(self, evt):
		if not self.outroCheckBox.IsChecked():
			self.outroSizer.Hide(self.outroAlarmLabel)
			self.outroSizer.Hide(self.endOfTrackAlarm)
		else:
			self.outroSizer.Show(self.outroAlarmLabel)
			self.outroSizer.Show(self.endOfTrackAlarm)
		self.Fit()

	def onIntroCheck(self, evt):
		if not self.introCheckBox.IsChecked():
			self.introSizer.Hide(self.introAlarmLabel)
			self.introSizer.Hide(self.songRampAlarm)
		else:
			self.introSizer.Show(self.introAlarmLabel)
			self.introSizer.Show(self.songRampAlarm)
		self.Fit()

	# Include profile flags such as instant profile string for display purposes.
	def displayProfiles(self, profiles):
		for index in xrange(len(profiles)):
			profiles[index] = getProfileFlags(profiles[index])
		return profiles


	# Load settings from profiles.
	def onProfileSelection(self, evt):
		# Don't rely on SPLConfig here, as we don't want to interupt the show.
		selection = self.profiles.GetSelection()
		# No need to look at the profile flag.
		selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
		# Play a tone to indicate active profile.
		if self.activeProfile == selectedProfile:
			tones.beep(512, 40)
		if selection == 0:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.triggerButton.Disable()
		else:
			self.renameButton.Enable()
			self.deleteButton.Enable()
			self.triggerButton.Enable()
		curProfile = getProfileByName(selectedProfile)
		self.outroCheckBox.SetValue(curProfile["IntroOutroAlarms"]["SayEndOfTrack"])
		self.endOfTrackAlarm.SetValue(long(curProfile["IntroOutroAlarms"]["EndOfTrackTime"]))
		self.onOutroCheck(None)
		self.introCheckBox.SetValue(curProfile["IntroOutroAlarms"]["SaySongRamp"])
		self.songRampAlarm.SetValue(long(curProfile["IntroOutroAlarms"]["SongRampTime"]))
		self.onIntroCheck(None)
		self.micAlarm.SetValue(long(curProfile["MicrophoneAlarm"]["MicAlarm"]))
		self.micAlarmInterval.SetValue(long(curProfile["MicrophoneAlarm"]["MicAlarmInterval"]))
		# 6.1: Take care of profile-specific column and metadata settings.
		self.metadataStreams = curProfile["MetadataStreaming"]["MetadataEnabled"]
		self.columnOrderCheckbox.SetValue(curProfile["ColumnAnnouncement"]["UseScreenColumnOrder"])
		self.columnOrder = curProfile["ColumnAnnouncement"]["ColumnOrder"]
		# 6.1: Again convert list to set.
		self.includedColumns = set(curProfile["ColumnAnnouncement"]["IncludedColumns"])

	# Profile controls.
	# Rename and delete events come from GUI/config profiles dialog from NVDA core.
	def onNew(self, evt):
		self.Disable()
		NewProfileDialog(self).Show()

	def onCopy(self, evt):
		self.Disable()
		NewProfileDialog(self, copy=True).Show()

	def onRename(self, evt):
		global SPLConfigPool, _SPLCache
		oldDisplayName = self.profiles.GetStringSelection()
		state = oldDisplayName.split(" <")
		oldName = state[0]
		index = self.profiles.Selection
		configPos = getProfileIndexByName(oldName)
		profilePos = self.profileNames.index(oldName)
		# Translators: The label of a field to enter a new name for a broadcast profile.
		with wx.TextEntryDialog(self, _("New name:"),
				# Translators: The title of the dialog to rename a profile.
				_("Rename Profile"), defaultValue=oldName) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			newName = api.filterFileName(d.Value)
		if oldName == newName: return
		newNamePath = newName + ".ini"
		newProfile = os.path.join(SPLProfiles, newNamePath)
		if oldName.lower() != newName.lower() and os.path.isfile(newProfile):
			# Translators: An error displayed when renaming a configuration profile
			# and a profile with the new name already exists.
			gui.messageBox(_("That profile already exists. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		oldNamePath = oldName + ".ini"
		oldProfile = os.path.join(SPLProfiles, oldNamePath)
		try:
			os.rename(oldProfile, newProfile)
		except WindowsError:
			pass
		if self.switchProfile == oldName:
			self.switchProfile = newName
			self.switchProfileRenamed = True
		# Be sure to update profile triggers.
		if oldName in self._profileTriggersConfig:
			self._profileTriggersConfig[newName] = self._profileTriggersConfig[oldName]
			del self._profileTriggersConfig[oldName]
		if self.activeProfile == oldName:
			self.activeProfile = newName
		self.profileNames[profilePos] = newName
		SPLConfigPool[configPos].name = newName
		SPLConfigPool[configPos].filename = newProfile
		_SPLCache[newName] = _SPLCache[oldName]
		del _SPLCache[oldName]
		if len(state) > 1: newName = " <".join([newName, state[1]])
		self.profiles.SetString(index, newName)
		self.profiles.Selection = index
		self.profiles.SetFocus()

	def onDelete(self, evt):
		# Prevent profile deletion in the midst of a broadcast, otherwise time-based profile switching flag will become inconsistent.
		# 7.1: Find a way to safely proceed via two-step verification if trying to delete currently active time-based profile.
		global _SPLTriggerEndTimer, _triggerProfileActive
		if (_SPLTriggerEndTimer is not None and _SPLTriggerEndTimer.IsRunning()) or _triggerProfileActive:
			gui.messageBox(_("Are you currently broadcasting a show? If so, please press SPL Assistant, F12 to switch back to a previously active profile before opening add-on settings to delete a profile."),
				_("Midst of a broadcast"), wx.OK | wx.ICON_ERROR, self)
			return
		index = self.profiles.Selection
		name = self.profiles.GetStringSelection().split(" <")[0]
		configPos = getProfileIndexByName(name)
		profilePos = self.profileNames.index(name)
		if gui.messageBox(
			# Translators: The confirmation prompt displayed when the user requests to delete a broadcast profile.
			_("Are you sure you want to delete this profile? This cannot be undone."),
			# Translators: The title of the confirmation dialog for deletion of a profile.
			_("Confirm Deletion"),
			wx.YES | wx.NO | wx.ICON_QUESTION, self
		) == wx.NO:
			return
		global SPLConfigPool, SPLSwitchProfile, SPLPrevProfile, _SPLCache
		path = SPLConfigPool[configPos].filename
		del SPLConfigPool[configPos]
		try:
			os.remove(path)
		except WindowsError:
			pass
		if name == self.switchProfile or name == self.activeProfile:
			self.switchProfile = None
			SPLPrevProfile = None
			self.switchProfileDeleted = True
		self.profiles.Delete(index)
		del self.profileNames[profilePos]
		del _SPLCache[name]
		if name in self._profileTriggersConfig:
			del self._profileTriggersConfig[name]
		# 6.3: Select normal profile if the active profile is gone.
		# 7.0: Consult profile names instead.
		try:
			self.profiles.Selection = self.profileNames.index(self.activeProfile)
		except ValueError:
			self.activeProfile = SPLConfigPool[0].name
			self.profiles.Selection = 0
		self.onProfileSelection(None)
		self.profiles.SetFocus()

	def onTriggers(self, evt):
		self.Disable()
		TriggersDialog(self, self.profileNames[self.profiles.Selection]).Show()

	# Obtain profile flags for a given profile.
	# This is a proxy to the module level profile flag retriever with custom strings/maps as arguments.
	def getProfileFlags(self, name):
		return getProfileFlags(name, active=self.activeProfile, instant=self.switchProfile, triggers=self._profileTriggersConfig, contained=True)

	# Handle flag modifications such as when toggling instant switch.
	# Unless given, flags will be queried.
	# This is a sister function to profile flags retriever.
	def setProfileFlags(self, index, action, flag, flags=None):
		profile = self.profileNames[index]
		if flags is None: flags = self.getProfileFlags(profile)
		action = getattr(flags, action)
		action(flag)
		self.profiles.SetString(index, profile if not len(flags) else "{0} <{1}>".format(profile, ", ".join(flags)))

	# Manage metadata streaming.
	def onManageMetadata(self, evt):
		self.Disable()
		MetadataStreamingDialog(self).Show()

	# Manage column announcements.
	def onManageColumns(self, evt):
		self.Disable()
		ColumnAnnouncementsDialog(self).Show()

	# Columns Explorer configuration.
	def onColumnsExplorer(self, evt):
		self.Disable()
		ColumnsExplorerDialog(self).Show()

	# Status announcement dialog.
	def onStatusAnnouncement(self, evt):
		self.Disable()
		SayStatusDialog(self).Show()

	# Advanced options.
	# See advanced options class for more details.
	def onAdvancedOptions(self, evt):
		self.Disable()
		AdvancedOptionsDialog(self).Show()

	# Reset settings to defaults.
	# This affects the currently selected profile.
	def onResetConfig(self, evt):
		if gui.messageBox(
		# Translators: A message to warn about resetting SPL config settings to factory defaults.
		_("Are you sure you wish to reset SPL add-on settings to defaults?"),
		# Translators: The title of the warning dialog.
		_("Warning"),wx.YES_NO|wx.NO_DEFAULT|wx.ICON_WARNING,self
		)==wx.YES:
			# Reset all profiles.
			# Save some flags from death.
			global SPLConfig, SPLConfigPool, SPLActiveProfile, _configDialogOpened, SPLSwitchProfile, SPLPrevProfile
			colRange = SPLConfig["ColumnExpRange"]
			resetAllConfig()
			SPLConfig = dict(_SPLDefaults7)
			SPLConfig["ActiveIndex"] = 0
			SPLActiveProfile = SPLConfigPool[0].name
			SPLConfig["ColumnExpRange"] = colRange
		if SPLSwitchProfile is not None:
			SPLSwitchProfile = None
		SPLPrevProfile = None
		_configDialogOpened = False
		self.Destroy()


# Open the above dialog upon request.
def onConfigDialog(evt):
	# 5.2: Guard against alarm dialogs.
	if _alarmDialogOpened:
		# Translators: Presented when an alarm dialog is opened.
		wx.CallAfter(gui.messageBox, _("An alarm dialog is already opened. Please close the alarm dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
	else: gui.mainFrame._popupSettingsDialog(SPLConfigDialog)

# Helper dialogs for add-on settings dialog.

# New broadcast profile dialog: Modification of new config profile dialog from NvDA Core.
class NewProfileDialog(wx.Dialog):

	def __init__(self, parent, copy=False):
		self.copy = copy
		if not self.copy:
			# Translators: The title of the dialog to create a new broadcast profile.
			dialogTitle = _("New Profile")
		else:
			# Translators: The title of the dialog to copy a broadcast profile.
			dialogTitle = _("Copy Profile")
		super(NewProfileDialog, self).__init__(parent, title=dialogTitle)
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label of a field to enter the name of a new broadcast profile.
		sizer.Add(wx.StaticText(self, label=_("Profile name:")))
		item = self.profileName = wx.TextCtrl(self)
		sizer.Add(item)
		mainSizer.Add(sizer)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select a base  profile for copying.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Base profile:"))
		self.baseProfiles = wx.Choice(self, wx.ID_ANY, choices=[profile.split(" <")[0] for profile in parent.profiles.GetItems()])
		try:
			self.baseProfiles.SetSelection(self.baseProfiles.GetItems().index(parent.profiles.GetStringSelection().split(" <")[0]))
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.baseProfiles)
		if not self.copy:
			sizer.Hide(label)
			sizer.Hide(self.baseProfiles)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.profileName.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global SPLConfigPool, _SPLCache
		profileNames = [profile.name for profile in SPLConfigPool]
		name = api.filterFileName(self.profileName.Value)
		if not name:
			return
		if name in profileNames:
			# Translators: An error displayed when the user attempts to create a profile which already exists.
			gui.messageBox(_("That profile already exists. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		namePath = name + ".ini"
		if not os.path.exists(SPLProfiles):
			os.mkdir(SPLProfiles)
		newProfilePath = os.path.join(SPLProfiles, namePath)
		SPLConfigPool.append(unlockConfig(newProfilePath, profileName=name))
		# Make the cache know this is a new profile.
		# If nothing happens to this profile, the newly created profile will be saved to disk.
		_SPLCache[name]["___new___"] = True
		if self.copy:
			newProfile = SPLConfigPool[-1]
			baseProfile = getProfileByName(self.baseProfiles.GetStringSelection())
			for setting in newProfile.keys():
				try:
					# 6.1/7.0: Only iterate through mutatable keys.
					if baseProfile[setting] != newProfile[setting]:
						newProfile[setting] = baseProfile[setting]
				except KeyError:
					pass
		parent = self.Parent
		parent.profileNames.append(name)
		parent.profiles.Append(name)
		parent.profiles.Selection = parent.profiles.Count - 1
		parent.onProfileSelection(None)
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Broadcast profile triggers dialog.
# This dialog is similar to NVDA Core's profile triggers dialog and allows one to configure when to trigger this profile.
class TriggersDialog(wx.Dialog):

	def __init__(self, parent, profile):
		# Translators: The title of the broadcast profile triggers dialog.
		super(TriggersDialog, self).__init__(parent, title=_("Profile triggers for {profileName}").format(profileName = profile))
		import calendar
		self.profile = profile
		self.selection = parent.profiles.GetSelection()
		# When referencing profile triggers, use the dictionary stored in the main add-on settings.
		# This is needed in order to discard changes when cancel button is clicked from the parent dialog.
		if profile in self.Parent._profileTriggersConfig:
			t = self.Parent._profileTriggersConfig[profile]
			d = "-".join([str(t[1]), str(t[2]).zfill(2), str(t[3]).zfill(2)])
			t = ":".join([str(t[4]).zfill(2), str(t[5]).zfill(2)])
			triggerText = "The next trigger is scheduled on {0} at {1}.".format(d, t)
		else:
			triggerText = "No triggers defined."

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		label = wx.StaticText(self, wx.ID_ANY, label=triggerText)
		sizer.Add(label)

		# Translators: The label of a checkbox to toggle if selected profile is an instant switch profile.
		self.instantSwitchCheckbox=wx.CheckBox(self,wx.NewId(),label=_("This is an &instant switch profile"))
		self.instantSwitchCheckbox.SetValue(parent.switchProfile == parent.profiles.GetStringSelection().split(" <")[0])
		sizer.Add(self.instantSwitchCheckbox, border=10,flag=wx.TOP)

		# Translators: The label of a checkbox to toggle if selected profile is a time-based profile.
		self.timeSwitchCheckbox=wx.CheckBox(self,wx.NewId(),label=_("This is a &time-based switch profile"))
		self.timeSwitchCheckbox.SetValue(profile in self.Parent._profileTriggersConfig)
		self.timeSwitchCheckbox.Bind(wx.EVT_CHECKBOX, self.onTimeSwitch)
		sizer.Add(self.timeSwitchCheckbox, border=10,flag=wx.TOP)
		mainSizer.Add(sizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		daysSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Day")), wx.HORIZONTAL)
		self.triggerDays = []
		for day in xrange(len(calendar.day_name)):
			triggerDay=wx.CheckBox(self, wx.NewId(),label=calendar.day_name[day])
			value = (64 >> day & self.Parent._profileTriggersConfig[profile][0]) if profile in self.Parent._profileTriggersConfig else 0
			triggerDay.SetValue(value)
			self.triggerDays.append(triggerDay)
		for day in self.triggerDays:
			daysSizer.Add(day)
			if not self.timeSwitchCheckbox.IsChecked(): daysSizer.Hide(day)
		mainSizer.Add(daysSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		timeSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Time")), wx.HORIZONTAL)
		self.hourPrompt = wx.StaticText(self, wx.ID_ANY, label="Hour")
		timeSizer.Add(self.hourPrompt)
		self.hourEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=23)
		self.hourEntry.SetValue(self.Parent._profileTriggersConfig[profile][4] if profile in self.Parent._profileTriggersConfig else 0)
		self.hourEntry.SetSelection(-1, -1)
		timeSizer.Add(self.hourEntry)
		self.minPrompt = wx.StaticText(self, wx.ID_ANY, label="Minute")
		timeSizer.Add(self.minPrompt)
		self.minEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.minEntry.SetValue(self.Parent._profileTriggersConfig[profile][5] if profile in self.Parent._profileTriggersConfig else 0)
		self.minEntry.SetSelection(-1, -1)
		timeSizer.Add(self.minEntry)
		self.durationPrompt = wx.StaticText(self, wx.ID_ANY, label="Duration in minutes")
		timeSizer.Add(self.durationPrompt)
		self.durationEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=1440)
		self.durationEntry.SetValue(self.Parent._profileTriggersConfig[profile][6] if profile in self.Parent._profileTriggersConfig else 0)
		self.durationEntry.SetSelection(-1, -1)
		timeSizer.Add(self.durationEntry)
		if not self.timeSwitchCheckbox.IsChecked():
			timeSizer.Hide(self.hourPrompt)
			timeSizer.Hide(self.hourEntry)
			timeSizer.Hide(self.minPrompt)
			timeSizer.Hide(self.minEntry)
			timeSizer.Hide(self.durationPrompt)
			timeSizer.Hide(self.durationEntry)
		mainSizer.Add(timeSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.instantSwitchCheckbox.SetFocus()

	def onOk(self, evt):
		global SPLTriggerProfile, triggerTimer
		parent = self.Parent
		# Handle instant switch checkbox.
		if self.instantSwitchCheckbox.Value:
			if parent.switchProfile is not None and (self.profile != parent.switchProfile):
				# Instant switch flag is set on another profile, so remove the flag first.
				parent.setProfileFlags(parent.profileNames.index(parent.switchProfile), "discard", _("instant switch"))
			parent.setProfileFlags(self.selection, "add", _("instant switch"))
			parent.switchProfile = self.profile
		else:
			parent.switchProfile = None
			parent.setProfileFlags(self.selection, "discard", _("instant switch"))
		# Now time-based profile checkbox.
		if self.timeSwitchCheckbox.Value:
			bit = 0
			for day in self.triggerDays:
				if day.Value: bit+=64 >> self.triggerDays.index(day)
			if bit:
				hour, min = self.hourEntry.GetValue(), self.minEntry.GetValue()
				duration = self.durationEntry.GetValue()
				if duplicateExists(parent._profileTriggersConfig, self.profile, bit, hour, min, duration):
					gui.messageBox(_("A profile trigger already exists for the entered time slot. Please choose a different date or time."),
						_("Error"), wx.OK | wx.ICON_ERROR, self)
					return
				# Change display name if there is no profile of this name registered.
				# This helps in preventing unnecessary calls to profile flags retriever, a huge time and memory savings.
				# Otherwise trigger flag will be added each time this is called (either this handler or the add-on settings' flags retriever must retrieve the flags set).
				if not self.profile in parent._profileTriggersConfig:
					parent.setProfileFlags(self.selection, "add", _("time-based"))
				parent._profileTriggersConfig[self.profile] = setNextTimedProfile(self.profile, bit, datetime.time(hour, min), duration=duration)
			else:
				# Er, did you specify a date?
				gui.messageBox(_("The time-based profile checkbox is checked but no switch dates are given. Please either specify switch date(s) or uncheck time-based profile checkbox."),
					_("Error"), wx.OK | wx.ICON_ERROR, self)
				return
		elif not self.timeSwitchCheckbox.Value and self.profile in self.Parent._profileTriggersConfig:
			del parent._profileTriggersConfig[self.profile]
			# Calling set profile flags with discard argument is always safe here.
			parent.setProfileFlags(self.selection, "discard", _("time-based"))
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

	# Disable date and time sizers when time switch checkbox is cleared and vice versa.
	def onTimeSwitch(self, evt):
		# Hack: Somehow, NVDA is not notified of state change for this checkbox, so force NVDA to report the new state.
		import eventHandler
		eventHandler.executeEvent("stateChange", api.getFocusObject())
		for prompt in self.triggerDays + [self.hourPrompt, self.hourEntry, self.minPrompt, self.minEntry, self.durationPrompt, self.durationEntry]:
			prompt.Show() if self.timeSwitchCheckbox.IsChecked() else prompt.Hide()
		self.Fit()

# Metadata reminder controller.
# Select notification/streaming URL's for metadata streaming.
_metadataDialogOpened = False

class MetadataStreamingDialog(wx.Dialog):
	"""A dialog to toggle metadata streaming quickly and from add-on settings dialog.
	"""
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _metadataDialogOpened:
			raise RuntimeError("An instance of metadata stremaing dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, func=None):
		inst = MetadataStreamingDialog._instance() if MetadataStreamingDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		MetadataStreamingDialog._instance = weakref.ref(self)

		super(MetadataStreamingDialog, self).__init__(parent, title=_("Metadata streaming options"))
		self.func = func

		# WX's CheckListBox isn't user friendly.
		# Therefore use checkboxes laid out across the top.
		self.checkedStreams = []
		# Add the DSP encoder checkbox first before adding other URL's.
		checkedDSP=wx.CheckBox(self,wx.NewId(),label="DSP encoder")
		if func:
			streaming = func(0, 36, ret=True)
			if streaming == -1: streaming += 1
			checkedDSP.SetValue(streaming)
		else: checkedDSP.SetValue(self.Parent.metadataStreams[0])
		self.checkedStreams.append(checkedDSP)
		# Now the rest.
		for url in xrange(1, 5):
			checkedURL=wx.CheckBox(self,wx.NewId(),label="URL {URL}".format(URL = url))
			if func:
				streaming = func(url, 36, ret=True)
				if streaming == -1: streaming += 1
				checkedURL.SetValue(streaming)
			else: checkedURL.SetValue(self.Parent.metadataStreams[url])
			self.checkedStreams.append(checkedURL)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		# First, a help text.
		if func is None: labelText=_("Select the URL for metadata streaming upon request.")
		else: labelText=_("Check to enable metadata streaming, uncheck to disable.")
		label = wx.StaticText(self, wx.ID_ANY, label=labelText)
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedStream in self.checkedStreams:
			sizer.Add(checkedStream)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		if self.func is not None:
			self.applyCheckbox=wx.CheckBox(self,wx.NewId(),label="&Apply streaming changes to the selected profile")
			self.applyCheckbox.SetValue(True)
			mainSizer.Add(self.applyCheckbox, border=10,flag=wx.TOP)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedStreams[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global _metadataDialogOpened
		if self.func is None: parent = self.Parent
		metadataEnabled = []
		for url in xrange(5):
			if self.func is None: parent.metadataStreams[url] = self.checkedStreams[url].Value
			else:
				dataLo = 0x00010000 if self.checkedStreams[url].Value else 0xffff0000
				self.func(dataLo | url, 36)
				if self.applyCheckbox.Value: metadataEnabled.append(self.checkedStreams[url].Value)
		if self.func is None:
			parent.profiles.SetFocus()
			parent.Enable()
		else:
			# 6.1: Store just toggled settings to profile if told to do so.
			if len(metadataEnabled): SPLConfig["MetadataStreaming"]["MetadataEnabled"] = metadataEnabled
		self.Destroy()
		_metadataDialogOpened = False
		return

	def onCancel(self, evt):
		global _metadataDialogOpened
		if self.func is None: self.Parent.Enable()
		self.Destroy()
		_metadataDialogOpened = False

# Column announcement manager.
# Select which track columns should be announced and in which order.
class ColumnAnnouncementsDialog(wx.Dialog):

	def __init__(self, parent):
		super(ColumnAnnouncementsDialog, self).__init__(parent, title=_("Manage column announcements"))

		# Same as metadata dialog (wx.CheckListBox isn't user friendly).
		# Gather values for checkboxes except artist and title.
		# 6.1: Split these columns into rows.
		self.checkedColumns = []
		for column in ("Duration", "Intro", "Category", "Filename"):
			checkedColumn=wx.CheckBox(self,wx.NewId(),label=column)
			checkedColumn.SetValue(column in self.Parent.includedColumns)
			self.checkedColumns.append(checkedColumn)
		self.checkedColumns2 = []
		for column in ("Outro","Year","Album","Genre","Mood","Energy"):
			checkedColumn=wx.CheckBox(self,wx.NewId(),label=column)
			checkedColumn.SetValue(column in self.Parent.includedColumns)
			self.checkedColumns2.append(checkedColumn)
		self.checkedColumns3 = []
		for column in ("Tempo","BPM","Gender","Rating","Time Scheduled"):
			checkedColumn=wx.CheckBox(self,wx.NewId(),label=column)
			checkedColumn.SetValue(column in self.Parent.includedColumns)
			self.checkedColumns3.append(checkedColumn)


		mainSizer = wx.BoxSizer(wx.VERTICAL)
		# First, a help text.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Select columns to be announced (artist and title are announced by default"))
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedColumn in self.checkedColumns:
			sizer.Add(checkedColumn)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedColumn in self.checkedColumns2:
			sizer.Add(checkedColumn)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedColumn in self.checkedColumns3:
			sizer.Add(checkedColumn)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select column announcement order.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Column &order:"))
		# WXPython Phoenix contains RearrangeList to allow item orders to be changed automatically.
		# Because WXPython Classic doesn't include this, work around by using a variant of list box and move up/down buttons.
		self.trackColumns= wx.ListBox(self, wx.ID_ANY, choices=parent.columnOrder)
		self.trackColumns.Bind(wx.EVT_LISTBOX,self.onColumnSelection)
		try:
			self.trackColumns.SetSelection(0)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.trackColumns)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		self.upButton = wx.Button(self, wx.ID_ANY, label=_("Move &up"))
		self.upButton.Bind(wx.EVT_BUTTON,self.onMoveUp)
		self.upButton.Disable()
		sizer.Add(self.upButton)
				# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		self.dnButton = wx.Button(self, wx.ID_ANY, label=_("Move &down"))
		self.dnButton.Bind(wx.EVT_BUTTON,self.onMoveDown)
		sizer.Add(self.dnButton)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedColumns[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.columnOrder = self.trackColumns.GetItems()
		# Make sure artist and title are always included.
		parent.includedColumns.add("Artist")
		parent.includedColumns.add("Title")
		for checkbox in self.checkedColumns + self.checkedColumns2 + self.checkedColumns3:
			action = parent.includedColumns.add if checkbox.Value else parent.includedColumns.discard
			action(checkbox.Label)
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

	def onColumnSelection(self, evt):
		selIndex = self.trackColumns.GetSelection()
		self.upButton.Disable() if selIndex == 0 else self.upButton.Enable()
		if selIndex == self.trackColumns.GetCount()-1:
			self.dnButton.Disable()
		else: self.dnButton.Enable()

	def onMoveUp(self, evt):
		tones.beep(1000, 200)
		selIndex = self.trackColumns.GetSelection()
		if selIndex > 0:
			selItem = self.trackColumns.GetString(selIndex)
			self.trackColumns.Delete(selIndex)
			self.trackColumns.Insert(selItem, selIndex-1)
			self.trackColumns.Select(selIndex-1)
			self.onColumnSelection(None)

	def onMoveDown(self, evt):
		tones.beep(500, 200)
		selIndex = self.trackColumns.GetSelection()
		if selIndex < self.trackColumns.GetCount()-1:
			selItem = self.trackColumns.GetString(selIndex)
			self.trackColumns.Delete(selIndex)
			self.trackColumns.Insert(selItem, selIndex+1)
			self.trackColumns.Select(selIndex+1)
			self.onColumnSelection(None)
			# Hack: Wen the last item is selected, forcefully move the focus to "move up" button.
			# This will cause NVDA to say "unavailable" as focus is lost momentarily. A bit anoying but a necessary hack.
			if self.FindFocus().GetId() == wx.ID_OK:
				self.upButton.SetFocus()

# Columns Explorer.
# Configure which column will be announced when SPL Assistnat, number keys are pressed.
class ColumnsExplorerDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of Columns Explorer configuration dialog.
		super(ColumnsExplorerDialog, self).__init__(parent, title=_("Columns Explorer"))

		# Gather column slots.
		# 7.0: First six slots are reserved for Studio 5.0x columns.
		self.columnSlots = []

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		# 7.0: Studio 5.0x columns.
		# 8.0: Remove the below code.
		oldStudioColumns = ["Artist", "Title", "Duration", "Intro", "Category", "Filename"]
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for slot in xrange(6):
			# Translators: The label for a setting in SPL add-on dialog to select column for this column slot.
			label = wx.StaticText(self, wx.ID_ANY, label=_("Slot {position}").format(position = slot+1))
			columns = wx.Choice(self, wx.ID_ANY, choices=oldStudioColumns)
			try:
				columns.SetSelection(oldStudioColumns.index(parent.exploreColumns[slot]))
			except:
				pass
			sizer.Add(label)
			sizer.Add(columns)
			self.columnSlots.append(columns)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# For Studio 5.10 and later.
		if SPLConfig["ColumnExpRange"] == (0, 10):
			sizer = wx.BoxSizer(wx.HORIZONTAL)
			for slot in xrange(6, 10):
				label = wx.StaticText(self, wx.ID_ANY, label=_("Slot {position}").format(position = slot+1))
				columns = wx.Choice(self, wx.ID_ANY, choices=_SPLDefaults7["ColumnAnnouncement"]["ColumnOrder"])
				try:
					columns.SetSelection(_SPLDefaults7["ColumnAnnouncement"]["ColumnOrder"].index(parent.exploreColumns[slot]))
				except:
					pass
				sizer.Add(label)
				sizer.Add(columns)
				self.columnSlots.append(columns)
			mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.columnSlots[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		for slot in xrange(len(self.columnSlots)):
			parent.exploreColumns[slot] = self.columnSlots[slot].GetStringSelection()
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Say status dialog.
# Houses options such as announcing cart names.
class SayStatusDialog(wx.Dialog):

	def __init__(self, parent):
		super(SayStatusDialog, self).__init__(parent, title=_("Status announcements"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		# Translators: the label for a setting in SPL add-on settings to announce scheduled time.
		self.scheduledForCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce &scheduled time for the selected track"))
		self.scheduledForCheckbox.SetValue(parent.scheduledFor)
		mainSizer.Add(self.scheduledForCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce listener count.
		self.listenerCountCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce &listener count"))
		self.listenerCountCheckbox.SetValue(parent.listenerCount)
		mainSizer.Add(self.listenerCountCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce currently playing cart.
		self.cartNameCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Announce name of the currently playing cart"))
		self.cartNameCheckbox.SetValue(parent.cartName)
		mainSizer.Add(self.cartNameCheckbox, border=10,flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to announce currently playing track name.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Track name announcement:"))
		# Translators: One of the track name announcement options.
		self.trackAnnouncements=[("True",_("automatic")),
		# Translators: One of the track name announcement options.
		("Background",_("while using other programs")),
		# Translators: One of the track name announcement options.
		("False",_("off"))]
		self.trackAnnouncementList= wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.trackAnnouncements])
		selection = (x for x,y in enumerate(self.trackAnnouncements) if y[0]==parent.playingTrackName).next()  
		try:
			self.trackAnnouncementList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.trackAnnouncementList)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.scheduledForCheckbox.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.scheduledFor = self.scheduledForCheckbox.Value
		parent.listenerCount = self.listenerCountCheckbox.Value
		parent.cartName = self.cartNameCheckbox.Value
		parent.playingTrackName = self.trackAnnouncements[self.trackAnnouncementList.GetSelection()][0]
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Advanced options
# This dialog houses advanced options such as using SPL Controller command to invoke SPL Assistant.
# More options will be added in 7.0.
# 7.0: Auto update check will be configurable from this dialog.
class AdvancedOptionsDialog(wx.Dialog):

	def __init__(self, parent):
		super(AdvancedOptionsDialog, self).__init__(parent, title=_("Advanced options"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A checkbox to toggle automatic add-on updates.
		self.autoUpdateCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Automatically check for add-on &updates"))
		self.autoUpdateCheckbox.SetValue(self.Parent.autoUpdateCheck)
		sizer.Add(self.autoUpdateCheckbox, border=10,flag=wx.TOP)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A checkbox to toggle if SPL Controller command can be used to invoke Assistant layer.
		self.splConPassthroughCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Allow SPL C&ontroller command to invoke SPL Assistant layer"))
		self.splConPassthroughCheckbox.SetValue(self.Parent.splConPassthrough)
		sizer.Add(self.splConPassthroughCheckbox, border=10,flag=wx.TOP)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to set keyboard layout for SPL Assistant.
		label = wx.StaticText(self, wx.ID_ANY, label=_("SPL Assistant command &layout:"))
		self.compatibilityLayouts=[("off","NVDA"),
		("jfw","JAWS for Windows"),
		("wineyes","Window-Eyes")]
		self.compatibilityList= wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.compatibilityLayouts])
		selection = (x for x,y in enumerate(self.compatibilityLayouts) if y[0]==self.Parent.compLayer).next()  
		try:
			self.compatibilityList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.compatibilityList)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.autoUpdateCheckbox.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.splConPassthrough = self.splConPassthroughCheckbox.Value
		parent.compLayer = self.compatibilityLayouts[self.compatibilityList.GetSelection()][0]
		parent.autoUpdateCheck = self.autoUpdateCheckbox.Value
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Additional configuration dialogs

# A common alarm dialog
# Based on NVDA core's find dialog code (implemented by the author of this add-on).
# Only one instance can be active at a given moment (code borrowed from GUI's exit dialog routine).
_alarmDialogOpened = False

# A common alarm error dialog.
def _alarmError():
	# Translators: Text of the dialog when another alarm dialog is open.
	gui.messageBox(_("Another alarm dialog is open."),_("Error"),style=wx.OK | wx.ICON_ERROR)

class SPLAlarmDialog(wx.Dialog):
	"""A dialog providing common alarm settings.
	This dialog contains a number entry field for alarm duration and a check box to enable or disable the alarm.
	"""

	# The following comes from exit dialog class from GUI package (credit: NV Access and Zahari from Bulgaria).
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _alarmDialogOpened:
			raise RuntimeError("An instance of alarm dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, setting, toggleSetting, title, alarmPrompt, alarmToggleLabel, min, max):
		inst = SPLAlarmDialog._instance() if SPLAlarmDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		SPLAlarmDialog._instance = weakref.ref(self)

		# Now the actual alarm dialog code.
		super(SPLAlarmDialog, self).__init__(parent, wx.ID_ANY, title)
		self.setting = setting
		self.toggleSetting = toggleSetting
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		alarmSizer = wx.BoxSizer(wx.HORIZONTAL)
		alarmMessage = wx.StaticText(self, wx.ID_ANY, label=alarmPrompt)
		alarmSizer.Add(alarmMessage)
		self.alarmEntry = wx.SpinCtrl(self, wx.ID_ANY, min=min, max=max)
		self.alarmEntry.SetValue(SPLConfig["IntroOutroAlarms"][setting])
		self.alarmEntry.SetSelection(-1, -1)
		alarmSizer.Add(self.alarmEntry)
		mainSizer.Add(alarmSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		self.toggleCheckBox=wx.CheckBox(self,wx.NewId(),label=alarmToggleLabel)
		self.toggleCheckBox.SetValue(SPLConfig["IntroOutroAlarms"][toggleSetting])
		mainSizer.Add(self.toggleCheckBox,border=10,flag=wx.BOTTOM)

		mainSizer.AddSizer(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.alarmEntry.SetFocus()

	def onOk(self, evt):
		global _alarmDialogOpened
		# Optimization: don't bother if Studio is dead and if the same value has been entered.
		if user32.FindWindowA("SPLStudio", None):
			newVal = self.alarmEntry.GetValue()
			newToggle = self.toggleCheckBox.GetValue()
			if SPLConfig["IntroOutroAlarms"][self.setting] != newVal: SPLConfig["IntroOutroAlarms"][self.setting] = newVal
			elif SPLConfig["IntroOutroAlarms"][self.toggleSetting] != newToggle: SPLConfig["IntroOutroAlarms"][self.toggleSetting] = newToggle
			# Apply alarm settings only.
			applySections(SPLConfig["ActiveIndex"], "/".join(["IntroOutroAlarms", self.setting]))
			applySections(SPLConfig["ActiveIndex"], "/".join(["IntroOutroAlarms", self.toggleSetting]))
		self.Destroy()
		_alarmDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _alarmDialogOpened
		_alarmDialogOpened = False


# Startup dialogs.

# Audio ducking reminder (NVDA 2016.1 and later).
class AudioDuckingReminder(wx.Dialog):
	"""A dialog to remind users to turn off audio ducking (NVDA 2016.1 and later).
	"""

	def __init__(self, parent):
		super(AudioDuckingReminder, self).__init__(parent, title=_("SPL Studio and audio ducking"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		# Translators: A message displayed if audio ducking should be disabled.
		label = wx.StaticText(self, wx.ID_ANY, label=_("NVDA 2016.1 and later allows NVDA to decrease volume of background audio including that of Studio. In order to not disrupt the listening experience of your listeners, please disable audio ducking by opening synthesizer dialog in NVDA and selecting 'no ducking' from audio ducking mode combo box or press NVDA+Shift+D."))
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A checkbox to turn off audio ducking reminder message.
		self.audioDuckingReminder=wx.CheckBox(self,wx.NewId(),label=_("Do not show this message again"))
		self.audioDuckingReminder.SetValue(not SPLConfig["Startup"]["AudioDuckingReminder"])
		sizer.Add(self.audioDuckingReminder, border=10,flag=wx.TOP)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.audioDuckingReminder.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		if self.audioDuckingReminder.Value:
			SPLConfig["Startup"]["AudioDuckingReminder"] = not self.audioDuckingReminder.Value
		self.Destroy()

# And to open the above dialog and any other dialogs.
def showStartupDialogs():
	try:
		import audioDucking
		if SPLConfig["Startup"]["AudioDuckingReminder"] and audioDucking.isAudioDuckingSupported():
			gui.mainFrame.prePopup()
			AudioDuckingReminder(gui.mainFrame).Show()
			gui.mainFrame.postPopup()
	except ImportError:
		pass


# Message verbosity pool.
# To be moved to its own module in add-on 7.0.
# This is a multimap, consisting of category, value and message.
# Most of the categories are same as confspec keys, hence the below message function is invoked when settings are changed.
def message(category, value):
	verbosityLevels = ("beginner", "advanced")
	ui.message(messagePool[category][value][verbosityLevels.index(SPLConfig["General"]["MessageVerbosity"])])

messagePool={
	"BeepAnnounce":
		{True:
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			(_("Status announcement beeps"),
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			_("Beeps")),
		False:
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			(_("Status announcement words"),
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			_("Words"))},
	"BrailleTimer":
		{"off":
			# Translators: A setting in braille timer options.
			(_("Braille timer off"), _("Off")),
		"outro":
			# Translators: A setting in braille timer options.
			(_("Braille track endings"),
						# Translators: A setting in braille timer options.
			_("Outro")),
		"intro":
			# Translators: A setting in braille timer options.
			(_("Braille intro endings"),
						# Translators: A setting in braille timer options.
			_("Intro")),
		"both":
			# Translators: A setting in braille timer options.
			(_("Braille intro and track endings"),
						# Translators: A setting in braille timer options.
			_("Both"))},
	"LibraryScanAnnounce":
		{"off":
			# Translators: A setting in library scan announcement options.
			(_("Do not announce library scans"), _("Off")),
		"ending":
			# Translators: A setting in library scan announcement options.
			(_("Announce start and end of a library scan"),
			_("Start and end only")),
		"progress":
			# Translators: A setting in library scan announcement options.
			(_("Announce the progress of a library scan"),
			_("Scan progress")),
		"numbers":
			# Translators: A setting in library scan announcement options.
			(_("Announce progress and item count of a library scan"),
			_("Scan count"))}}
