# SPL Studio Miscellaneous User Interfaces
# An app module and global plugin package for NVDA
# Copyright 2015 Joseph Lee and others, released under GPL.
# Miscellaneous functions and user interfaces
# Split from config module in 2015.

import ctypes
import weakref
import gui
import wx
from NVDAObjects.IAccessible import sysListView32
from winUser import user32, sendMessage
import winKernel

# Locate column content.
# Given an object and the column number, locate text in the given column.
# This is the module level version of column content getter found in the app module.
# This is used by the track item class as well as in track finder.
# In track finder, this is used when encountering the track item but NVDA says otherwise.
def _getColumnContent(obj, col):
	# Borrowed from SysListView32 implementation.
	buffer=None
	processHandle=obj.processHandle
	sizeofLVITEM = ctypes.sizeof(sysListView32.LVITEM)
	internalItem=winKernel.virtualAllocEx(processHandle,None,sizeofLVITEM,winKernel.MEM_COMMIT,winKernel.PAGE_READWRITE)
	try:
		internalText=winKernel.virtualAllocEx(processHandle,None,520,winKernel.MEM_COMMIT,winKernel.PAGE_READWRITE)
		try:
			item=sysListView32.LVITEM(iItem=obj.IAccessibleChildID-1,mask=sysListView32.LVIF_TEXT|sysListView32.LVIF_COLUMNS,iSubItem=col,pszText=internalText,cchTextMax=260)
			winKernel.writeProcessMemory(processHandle,internalItem,ctypes.byref(item),sizeofLVITEM,None)
			len = sendMessage(obj.windowHandle,sysListView32.LVM_GETITEMTEXTW, (obj.IAccessibleChildID-1), internalItem)
			if len:
				winKernel.readProcessMemory(processHandle,internalItem,ctypes.byref(item),sizeofLVITEM,None)
				buffer=ctypes.create_unicode_buffer(len)
				winKernel.readProcessMemory(processHandle,item.pszText,buffer,ctypes.sizeof(buffer),None)
		finally:
			winKernel.virtualFreeEx(processHandle,internalText,0,winKernel.MEM_RELEASE)
	finally:
		winKernel.virtualFreeEx(processHandle,internalItem,0,winKernel.MEM_RELEASE)
	return buffer.value if buffer else None

# A common dialog for Track Finder
_findDialogOpened = False

# Track Finder error dialog.
# This will be refactored into something else.
def _finderError():
	# Translators: Text of the dialog when another find dialog is open.
	gui.messageBox(_("Another find dialog is open."),_("Error"),style=wx.OK | wx.ICON_ERROR)

class SPLFindDialog(wx.Dialog):

	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, obj, text, title, columnSearch=False):
		inst = SPLFindDialog._instance() if SPLFindDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		SPLFindDialog._instance = weakref.ref(self)

		super(SPLFindDialog, self).__init__(parent, wx.ID_ANY, title)
		self.obj = obj
		self.columnSearch = columnSearch
		if not columnSearch:
			findPrompt = _("Enter the name or the artist of the track you wish to &search")
		else:
			findPrompt = _("Enter text to be &searched in a column")

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		findSizer = wx.BoxSizer(wx.HORIZONTAL)
		findMessage = wx.StaticText(self, wx.ID_ANY, label=findPrompt)
		findSizer.Add(findMessage)
		self.findEntry = wx.TextCtrl(self, wx.ID_ANY)
		self.findEntry.SetValue(text)
		findSizer.Add(self.findEntry)
		mainSizer.Add(findSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		if columnSearch:
			columnSizer = wx.BoxSizer(wx.HORIZONTAL)
			# Translators: The label in track finder to search columns.
			label = wx.StaticText(self, wx.ID_ANY, label=_("C&olumn to search:"))
			left = 1 if obj.appModule.productVersion >= "5.10" else 0
			headers = [header.name for header in obj.parent.children[-1].children[left:]]
			self.columnHeaders = wx.Choice(self, wx.ID_ANY, choices=headers)
			try:
				self.columnHeaders.SetSelection(0)
			except:
				pass
			columnSizer.Add(label)
			columnSizer.Add(self.columnHeaders)
			mainSizer.Add(columnSizer, border=10, flag=wx.BOTTOM)

		mainSizer.AddSizer(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.findEntry.SetFocus()

	def onOk(self, evt):
		global _findDialogOpened
		text = self.findEntry.GetValue()
		# Studio, are you alive?
		if user32.FindWindowA("SPLStudio", None) and text:
			appMod = self.obj.appModule
			column = self.columnHeaders.Selection if self.columnSearch else None
			if column and appMod.productVersion >= "5.10": column+=1
			startObj = self.obj
			if text == appMod.findText: startObj = startObj.next
			# If this is called right away, we land on an invisible window.
			wx.CallLater(100, appMod.trackFinder, text, startObj, column=column)
		self.Destroy()
		_findDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _findDialogOpened
		_findDialogOpened = False
