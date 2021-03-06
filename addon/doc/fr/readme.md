# StationPlaylist Studio #

* Auteurs: Geoff Shang, Joseph Lee et d'autres contributeurs.
* Télécharger [version stable][1]
* Télécharger [la version de développement][2]

Ce module complémentaire améliore l'utilisation de Station Playlist Studio,
mais il fournit aussi des utilitaires pour contrôler le Studio où que vous
soyez.

Pour plus d’informations sur le module complémentaire, lisez le [guide du
module complémentaire][4]. Pour les développeurs cherchant à savoir comment
construire le module complémentaire, voir buildInstructions.txt situé à la
racine du code source du module complémentaire du référentiel.

NOTES IMPORTANTES :

* Ce module complémentaire nécessite NVDA 2017.4 ou version ultérieure et
  StationPlaylist Studio 5.10 ou version ultérieure.
* Si vous utilisez Windows 8 ou ultérieur, pour une meilleure expérience,
  désactiver le Mode d'atténuation audio.
* le module complémentaire 8.0/16.10 requiert Studio 5.10 ou une version
  ultérieure. Pour les diffusions utilisant Studio 5.0x et/ou Windows XP,
  Vista ou 7 sans Service Pack 1, une [version prenant en charge le
  long-term][3] (15.x) est disponible. La dernière version stable prenant en
  charge les versions de Windows antérieures à la 7 Service Pack 1 est la
  17.11.2.
* À partir de 2018, [les journal des changements des anciennes versions du
  module complémentaire][5] seront trouvés sur GitHub. Ce fichier readme
  ajoutera les changements depuis la version 5.0 (à partir de 2015).
* Certaines fonctionnalités du module complémentaire (notamment la mise à
  jour de modules complémentaires) ne fonctionneront pas dans certaines
  conditions, notamment l'exécution de NVDA en mode sécurisé.
* En raison de limitations techniques, vous ne pouvez pas installer ou
  utiliser ce module complémentaire sur la version Windows Store de NVDA.

## Raccourcis clavier

* Alt+Maj+T depuis la fenêtre de Studio : annonce le temps écoulé pour la
  piste en cours de lecture.
* Contrôle+Alt+T (glissement à deux doigts vers le bas en mode tactile SPL)
  depuis la fenêtre de Studio : annoncer le temps restant pour la piste en
  cours de lecture.
* NVDA+Maj+F12 (glissement à deux doigts vers le haut en mode tactile SPL)
  depuis la fenêtre de Studio: annonce le temps de diffusion tel que 5
  minutes en haut de l'heure. Appuyez deux fois sur cette commande pour
  annoncer les minutes et les secondes jusqu'au début de l'heure.
* Alt+NVDA+1 (glissement à deux doigts vers la droite en mode SPL) depuis la
  fenêtre de Studio: Ouvre la boîte de dialogue  paramètre fin de piste.
* Alt+NVDA+2 (glissement à deux doigts vers la gauche en mode tactile SPL)
  depuis la fenêtre de Studio: Ouvre la boîte de dialogue  paramètre alarme
  chanson intro.
* Alt+NVDA+3 depuis la fenêtre de Studio : Basculer l'explorateur de chariot
  pour apprendre les assignations de chariot.
* Alt+NVDA+4 depuis la fenêtre de Studio : Ouvre le dialogue alarme
  microphone.
* Contrôle+NVDA+f depuis la fenêtre de Studio : Ouvre un dialogue pour
  chercher une piste en se basant sur l'artiste ou le nom de la
  chanson. Appuyez  sur NVDA+F3 pour chercher vers l'avant ou appuyez sur
  NVDA+Maj+F3 pour rechercher vers l'arrière.
* Alt+NVDA+R depuis la fenêtre de Studio : parcourt les paramètres d'annonce
  du balayage dans la bibliothèque.
* Contrôle+Maj+X depuis la fenêtre de Studio : Parcourt les paramètres du
  minuteur braille.
* Contrôle+Alt+flèche gauche/droite (alors que  a été mis en focus sur une
  piste) : Annoncer colonne de piste précédente/suivante.
* Contrôle+Alt+flèche haut/bas (alors que  a été mis en focus sur une piste)
  : Déplacer vers la piste précédente ou suivante et annoncer des colonnes
  spécifiques (indisponible dans le module complémentaire 15.x).
* Contrôle+NVDA+1 jusqu'à 0 (6 pour Studio 5.0x) : Annoncer le contenu de la
  colonne pour une colonne spécifiée.
* Alt+NVDA+C alors que  a été mis en focus sur une piste : annonce les
  commentaires de piste le cas échéant.
* Alt+NVDA+0 depuis la fenêtre de Studio : Ouvre le dialogue de
  configuration du module complémentaire Studio.
* Contrôle+NVDA+- (tiret) depuis la fenêtre de Studio : Envoyez vos
  commentaires au développeur du module complémentaire en utilisant le
  client de messagerie par défaut.
* Alt+NVDA+F1: Ouvre le dialogue de bienvenue.

## Commandes non assignées

Les commandes suivantes ne sont pas assignées par défaut ; si vous souhaitez
les assigner, utilisez le dialogue Gestes de commandes pour ajouter des
commandes personnalisées.

* Basculement vers la fenêtre SPL Studio depuis n'importe quel programme.
* Couche Contrôleur SPL.
* Annonçant le statut de Studio, comme la lecture de pistes à partir
  d'autres programmes.
* Couche Assistant SPL depuis SPL Studio.
* Annoncer le temps y compris les secondes depuis SPL Studio.
* Annonce de la température.
* Annonce du titre de la piste suivante si planifié.
* Annonçant le titre de la piste en cours de lecture.
* Marquage de piste en cours pour le début de l'analyse de durée de piste.
* Effectuer des analyses de durée de piste.
* Prendre des instantanés de playlist
* Recherche de texte dans des colonnes spécifiques.
* Trouver des piste avec une durée qui se situe dans un intervalle donné via
  la recherche de l'intervalle de temps.
* Activer ou désactiver les métadonnées en streaming rapidement.

## Commandes supplémentaires lors de l'utilisation des encodeurs de Sam ou SPL

Les commandes suivantes sont disponibles lorsque vous utilisez les encodeurs
de Sam ou de SPL :

* F9 : Se connecter à un serveur de streaming.
* F10 (Encodeur SAM uniquement) : Se déconnecter d'un serveur de streaming.
* Contrôle+F9/Contrôle+F10 (encodeur SAM uniquement) : Connecter ou
  déconnecter tous les encodeurs, respectivement.
* F11 : Détermine si NVDA bascule vers la fenêtre Studio pour l'encodeur
  sélectionné  si connecté.
* Maj+F11: Détermine si Studio lit la première piste sélectionnée lorsque
  l'encodeur est connecté à un serveur de streaming.
* Contrôle+F11 : Active ou désactive le contrôle en arrière-plan de
  l'encodeur sélectionné.
* F12 :: Ouvre un dialogue de saisie d'une étiquette personnalisée pour le
  flux ou l'encodeur sélectionné.
* Contrôle+F12 : Ouvre un dialogue pour sélectionner l'encodeur que vous
  avez supprimé (afin de réaligner les étiquettes de flux et les paramètres
  de l'encodeur).
* Alt+NVDA+0 : Ouvre la boîte de dialogue paramètres  de l'encodeur pour
  configurer des options telles que l'étiquette de flux.

De plus, les commandes pour visualiser la colonne sont disponibles, y
compris :

* Contrôle+NVDA+1 : Position de l'encodeur.
* Contrôle+NVDA+2 : étiquette de flux.
* Contrôle+NVDA+3 depuis l'Encodeur SAM : Format de l'Encodeur.
* Contrôle+NVDA+3 depuis l'Encodeur SPL : Paramètres de l'encodeur.
* Contrôle+NVDA+4 depuis l'Encodeur SAM : Statut de la connexion de
  l'encodeur.
* Contrôle+NVDA+4 depuis l'Encodeur SPL : Statut de la connexion ou du taux
  de transfert.
* Contrôle+NVDA+5 depuis l'Encodeur SAM : Description du statut de la
  connexion.

## Couche Assistant SPL

Cette couche de commandes vous permet d'obtenir différents statuts sur SPL
Studio, comme si une piste est en cours de lecture, la durée totale de
toutes les pistes pour l'heure et ainsi de suite. De n'importe quelle
fenêtre de SPL Studio appuyez sur la commande couche Assistant SPL, puis
appuyez sur une des touches dans la liste ci-dessous (une ou plusieurs
commandes sont exclusives a la visionneuse de playlist). Vous pouvez
également configurer NVDA pour émuler les commandes des autres lecteurs
d’écran.

Les commandes disponibles sont :

* A : Automatisation.
* C (Maj+C dans la disposition de JAWS et Window-Eyes) : Titre pour la piste
  en cours de lecture.
* C (disposition JAWS et Window-Eyes) : Bascule l'explorateur de chariot
  (visionneuse de playlist uniquement).
* D (R dans la disposition de JAWS) : Durée restante pour la playlist (si un
  message d’erreur est donné, se déplacer vers la visionneuse de playlist et
  puis tapez cette commande).
* E (G dans la disposition de Window-Eyes) : Statut de métadonnées en
  streaming.
* Maj+1 jusqu'à maj+4, maj+0 : Statut de Métadonnées individuelles en
  streaming URLs (0 est pour l'encodeur DSP).
* E (disposition de Window-Eyes) : Temps écoulé pour la piste en cours de
  lecture.
* F : Recherche de piste (visionneuse de playlist uniquement).
* H : Durée de la musique pour la tranche horaire en cours.
* Maj+H : Durée des pistes restantes pour la tranche horaire.
* I (L dans la disposition de JAWS ou Window-Eyes) : Nombre d'auditeurs.
* K : Se déplacer à la piste marquée (visionneuse de playlist uniquement).
* Contrôle+K : Définir la piste en cours comme le marqueur de position de
  piste (visionneuse de playlist uniquement).
* L (Maj+L dans la  disposition de JAWS et Window-Eyes) : Entrée ligne.
* M : Microphone.
* N : Titre pour la piste suivante planifié.
* P : Statut (en cours de lecture ou arrêté).
* Maj+P : Hauteur de la piste actuelle.
* R (Maj+E dans la disposition  de JAWS et Window-Eyes) : Enregistrer dans
  un fichier activé/désactivé.
* Maj+R : Contrôle du balayage de la bibliothèque en cours.
* S : Piste débute (planifié).
* Maj+S : Durée jusqu'à la piste sélectionnée qui va être jouer (piste
  débute dans).
* T : Mode édition/insertion chariot activé/désactivé.
* U: temps de fonctionnement Studio.
* Contrôle+Maj+U : Rechercher les mises à jour du module complémentaire.
* W: Météo et température si configurée.
* Y: Statut de la modification de la playlist.
* 1 jusqu'à 0 (6 pour Studio 5.0x) : Annoncer le contenu de la colonne pour
  une colonne spécifiée.
* F8 : Prendre des instantanés de playlist (nombre de pistes, piste la plus
  longue, etc.).
* Maj+F8 : Demander des transcriptions de playlist dans de nombreux formats.
* F9 : Marquer la piste en cours pour le début de l'analyse de playlist
  (visionneuse de playlist uniquement).
* F10 : Effectuer une analyse de durée de piste (visionneuse de playlist
  uniquement).
* F12 : basculer entre un profil en cours et un profil prédéfini.
* F1: Aide couche.
* Maj+F1 : Ouvre le guide de l'utilisateur en ligne.

## Contrôleur SPL

Le contrôleur SPL est un ensemble de commandes couches que vous pouvez
utiliser pour contrôler SPL Studio de n'importe où. Appuyez sur la commandes
couche Contrôleur SPL, et NVDA dira, "Contrôleur SPL." Appuyez sur une autre
commande pour contrôler divers paramètres Studio comme activer/désactiver un
microphone ou lire la piste suivante.

Les commandes disponibles pour le Contrôleur SPL sont:

* Appuyez sur P pour lire la suivante piste sélectionnée.
* Appuyez sur U pour mettre en pause ou pour reprendre la lecture.
* Appuyer sur S pour arrêter la piste avec fondu enchaîné, ou pour arrêter
  la piste instantanément, appuyez sur T.
* Appuyer sur M ou Maj+M pour activer ou désactiver le microphone,
  respectivement, ou appuyez sur N pour activer le microphone sans fondu.
* Appuyer sur A pour activer l'automatisation ou Maj+A pour désactiver
  celle-ci.
* Appuyer sur L pour activer l'entrée ligne ou Maj+L pour désactiver
  celle-ci.
* Appuyez sur R pour entendre le temps restant pour la piste en cours de
  lecture.
* Appuyez sur Maj+R pour obtenir un rapport sur  l'avancement du balayage de
  la bibliothèque.
* Appuyez sur C pour laisser NVDA annoncer le nom et la durée de la piste en
  cours de lecture.
* Appuyez sur Maj+C pour laisser NVDA annoncer le nom et la durée de la
  prochaine piste, le cas échéant.
* Appuyez sur E pour obtenir un nombre et des étiquettes pour les encodeurs
  étant contrôlés.
* Appuyez sur I pour obtenir le nombre d'auditeurs.
* Appuyer sur Q pour obtenir diverses informations du statut de Studio, y
  compris si une piste est en cours de lecture, le microphone est activé et
  d'autres.
* Appuyez sur les touches de chariot (F1, Contrôle+1, par exemple) pour lire
  les chariots assignés à partir de n'importe où.
* Appuyez sur H pour afficher un dialogue d'aide répertoriant les commandes
  disponibles.

## Alarmes de la piste

Par défaut, NVDA jouera un bip si il y'a cinq secondes restantes dans la
piste (outro) et/ou intro. Pour configurer cette valeur aussi bien quant à
les activer ou désactiver, appuyer sur Alt+NVDA+1 ou Alt+NVDA+2 pour ouvrir
les boîtes de dialogues fin de piste et la montée de la chanson,
respectivement. De plus, Utiliser la boîte de dialogue paramètres du module
complémentaire Studio pour configurer si vous entendrez un bip, un message
ou tous les deux lorsque les alarmes sont basculés sur activé.

## Alarme microphone

Vous pouvez demander à NVDA de lire un son lorsque le microphone est actif
depuis un certain temps. Appuyez sur Alt+NVDA+4 pour configurer l'heure de
l'alarme en secondes (0 désactive celui-ci).

## Chercheur de piste

Si vous souhaitez trouver rapidement une chanson par artiste ou par nom de
chanson, depuis la liste de piste, appuyez sur Contrôle+NVDA+F. Tapez le nom
de l'artiste ou le nom de la chanson. NVDA va vous placer soit à la chanson
Si cell-ci est trouvé ou il affichera une erreur si elle ne trouve pas la
chanson que vous recherchez. Pour trouver une chanson ou un artiste
précédemment entrée, appuyez sur NVDA+F3 ou NVDA+Maj+F3 Pour trouver en
avant ou en arrière.

Remarque: le Chercheur de piste est sensible à la casse.

## Explorateur de Chariot

Selon l'édition, SPL Studio permet d'assigné jusq'à 96 chariots pendant la
lecture. NVDA vous permet d'entendre quel chariot ou jingle est assigné à
ces commandes.

Pour apprendre les assignations de chariot, depuis SPL Studio, appuyez sur
Alt+NVDA+3. Appuyant une fois sur la commande chariot il vous dira à quel
jingle est assignée à la commande. Appuyant deux fois sur la commande il
jouera le jingle. appuyez sur Alt+NVDA+3 pour quitter l'explorateur de
chariot. Consultez la documentation du module complémentaire pour plus
d'informations sur l'explorateur de chariot.

## Analyse de durée de piste

Pour obtenir la longueur pour jouer les pistes sélectionnés, marquer la
piste en cours pour le début de l'analyse de durée de piste (Assistant SPL,
F9), puis appuyer sur Assistant SPL, F10 lorsque vous atteignez la fin de la
sélection.

## Explorateur de Colonnes

En appuyant sur Contrôle+NVDA+1 jusqu'à 0 (6 pour Studio 5.0x) ou Assistant
SPL, 1 jusqu'à 0 (6 pour Studio 5.01 ou version antérieure), vous pouvez
obtenir le contenu des colonnes spécifiques. Par défaut ce sont artiste,
titre, durée, intro, catégorie et nom du fichier (Studio 5.10 ajoute année,
album, genre et heure prévue). Vous pouvez configurer les colonnes qui
seront explorées via le dialogue Explorateur de Colonnes trouvé dans le
dialogue Paramètres module complémentaire.

## Instantanés de playlist

Vous pouvez appuyer sur Assistant SPL , F8 étant focalisée sur une playlist
dans Studio pour obtenir diverses statistiques sur une playlist, y compris
le nombre de pistes dans la playlist, la piste la plus longue, les meilleurs
artistes et ainsi de suite.

## Transcriptions de Playlist

En appuyant sur Assistant SPL, Maj+F8 présentera une boîte de dialogue pour
vous permettre de demander des transcriptions de playlist dans de nombreux
formats, y compris dans un format de texte brut, un tableau HTML ou une
liste.

## Boîte de dialogue configuration

Depuis la fenêtre studio, vous pouvez appuyer sur Alt+NVDA+0 pour ouvrir la
boîte de dialogue configuration du module complémentaire. Sinon, allez dans
le menu préférences de NVDA et sélectionnez l'élément Paramètres SPL
Studio. Cette boîte de dialogue est également utilisé pour gérer les profils
de diffusion.

## Mode tactile SPL

Si vous utilisez Studio sur un ordinateur possédant un écran tactile
fonctionnant sous Windows 8 ou version ultérieure et NVDA 2012.3 ou version
ultérieure installé, vous pouvez exécuter certaines commandes Studio depuis
un écran tactile. Tout d'abord utiliser une tape à trois doigts pour
basculer en mode SPL, puis utilisez les commandes tactile énumérées
ci-dessus pour exécuter des commandes.

## Version 18.05

* Ajout de la possibilité de prendre des instantanés partiels de
  playlist. Cela peut être fait en définissant la plage d'analyse (Assistant
  SPL, F9 au début de la plage d'analyse) et en déplaçant vers un autre
  élément et en exécutant la commande instantanés de playlist.
* Ajout d'une nouvelle commande dans l'Assistant SPL pour demander des
  transcriptions de playlist dans un certain nombre de formats
  (Maj+F8). Ceux-ci incluent du texte brut, un tableau HTML ou une liste
  HTML.
* Diverses fonctions d'analyse des playlist, telles que l'analyse de durée
  de piste et les instantanés de playlist, sont désormais regroupées sous le
  thème "Analyseur de Playlist".

## Version 18.04.1

* NVDA ne cessera plus de démarrer le compte à rebours pour les profils de
  diffusion basés sur l'heure si NVDA avec wxPython 4 toolkit installé est
  en cours d'utilisation.

## Version 18.04

* Des modifications ont été apportées pour rendre la fonction de
  vérification des mises à jour du module complémentaire plus fiable, en
  particulier si la vérification automatique des mises à jour du module
  complémentaire est activée.
* NVDA émet une tonalité pour indiquer le début du balayage de la
  bibliothèque lorsqu'il est configuré pour lire des bips pour diverses
  annonces.
* NVDA démarre l'analyse de la bibliothèque en arrière-plan si l'analyse de
  la bibliothèque est démarrée à partir du dialogue Options de Studio ou au
  démarrage.
* Tapoter deux fois sur une piste sur un ordinateur à écran tactile ou si
  vous exécutez une commande d'action par défaut, la piste sera sélectionnée
  et va déplacer le focus système sur celle-ci.
* Lorsque vous prenez des instantanés de playlist (Assistant SPL, F8), si
  une playlist contient uniquement des marqueurs d'heure, elle résout
  plusieurs problèmes pour lesquels NVDA ne semblait pas prendre
  d'instantanés.

## Version 18.03/15.14-LTS

* Si NVDA est configuré pour annoncer l'état de la diffusion des métadonnées
  au démarrage de Studio, NVDA respectera ce paramètre et n'annoncera plus
  l'état de diffusion lors du basculement vers et à partir du changement de
  profil immédiat.
* Si le basculement vers et à partir d'un changement de profil immédiat et
  NVDA est configuré pour annoncer l'état de la diffusion des métadonnées à
  chaque fois que cela se produit, NVDA n'annoncera plus ces informations
  plusieurs fois lors du basculement rapide des profils.
* NVDA se rappellera de basculer au profil basé sur l'heure approprié (si
  défini pour un affichage) après que NVDA redémarre plusieurs fois pendant
  les diffusions.
* Si un profil basé sur l'heure avec la durée du profil est activé et que le
  dialogue paramètres du module complémentaire est ouvert et fermé, NVDA
  retournera au profil d'origine une fois le profil basé sur l'heure
  terminée.
* Si un profil basé sur l'heure est actif (en particulier pendant les
  diffusions), il ne sera pas possible de modifier les déclencheurs de
  profil de diffusion via le dialogue Paramètres du module complémentaire.

## Version 18.02/15.13-LTS

* 18.02 : En raison de modifications internes apportées pour prendre en
  charge les points d'extension et d'autres fonctionnalités, NVDA 2017.4 est
  requis.
* La mise à jour du module complémentaire ne sera pas possible dans certains
  cas. Cela inclut l'exécution de NVDA à partir du code source ou avec le
  mode sécurisé activé. La vérification du mode sécurisé s'applique
  également à la 15.13-LTS.
* Si des erreurs se produisent lors de la vérification des mises à jour,
  celles-ci seront sauvegardées et NVDA vous conseillera de lire le journal
  (log) de NVDA pour plus de détails.
* Dans les paramètres du module complémentaire, divers paramètres de mise à
  jour dans la section des paramètres avancés, tels que l'intervalle de mise
  à jour, ne seront pas affichés si la mise à jour des modules
  complémentaires n'est pas prise en charge.
* NVDA ne semblera plus se bloquer ou ne fera plus rien lors du basculement
  à un changement de profil immédiat ou à un profil basé sur l'heure et NVDA
  est configuré pour annoncer l'état de diffusion des métadonnées.

## Version 18.01/15.12-LTS

* Lors de l'utilisation de la disposition de JAWS pour l'Assistant SPL, la
  commande pour rechercher les mises à jour (Contrôle+Maj+U) fonctionne
  désormais correctement.
* Lorsque vous modifiez les paramètres alarme microphone via le dialogue
  alarme (Alt+NVDA+4), des modifications telles que l'activation de l'alarme
  et la modification de l'intervalle d'alarme sont appliquées à la fermeture
  du dialogue.

## Version 17.12

* Windows 7 Service Pack 1 ou ultérieur est requis.
* Plusieurs fonctionnalités du module complémentaire ont été améliorées avec
  des points d'extension. Cela permet au microphone alarm et à la
  fonctionnalité des métadonnées en streaming de répondre aux changements
  dans les profils de diffusion. Cela nécessite NVDA 2017.4.
* Lorsque Studio se ferme, divers dialogues du module complémentaire tels
  que les paramètres du module complémentaire, les dialogues d'alarme et
  autres se ferment automatiquement. Cela nécessite NVDA 2017.4.
* Ajout d'une nouvelle commande dans la Couche Contrôleur SPL pour annoncer
  le nom de la prochaine piste, le cas échéant (Maj+C).
* Vous pouvez maintenant appuyer sur les touches du chariot (F1, par
  exemple) après avoir entrée la Couche Contrôleur SPL pour lire les
  chariots assignés de n'importe où.
* En raison des changements introduits dans la boîte à outils GUI de
  wxPython 4, le dialogue pour effacer les étiquettes de flux est maintenant
  une zone de liste déroulante au lieu d'un champ d'entrée de nombre.

## Version 17.11.2

Ceci est la dernière version stable à prendre en charge Windows XP, Vista et
7 sans Service Pack 1. La prochaine version stable pour ces versions de
Windows sera une version 15.x LTS.

* Si vous utiliser les versions de Windows antérieures à Windows 7 Service
  Pack 1, vous ne pouvez pas basculer vers les canaux de développement.

## Version 17.11.1/15.11-LTS

* NVDA ne lira plus les tonalités d'erreur ou ne semblera rien faire lors de
  l'utilisation des touches  Contrôle+Alt+flèches gauche ou droite pour
  naviguer dans les colonnes de l'Outil de Piste 5.20 avec une piste
  chargée. En raison de cette modification, lorsque vous utilisez Studio
  5.20, la version 48 ou ultérieure est requise.

## Version 17.11/15.10-LTS

* Premier support de StationPlaylist Studio 5.30.
* Si l'alarme microphone et/ou la minuterie d'intervalle est activée et si
  Studio quitte pendant que le microphone est activé, NVDA ne jouera plus de
  tonalité d'alarme microphone de partout.
* Lors de la suppression de profils de diffusion et si un autre profil se
  trouve être un changement de profil immédiat, l'indicateur de changement
  immédiat ne sera pas supprimé du changement de profil.
* Si vous supprimez un profil actif qui n'est pas un changement immédiat ou
  un profil basé sur l'heure, NVDA demandera une fois de plus une
  confirmation avant de continuer.
* NVDA appliquera les paramètres corrects pour les paramètres alarme
  microphone lors des changements de profils via le dialogue de Paramètres
  du module complémentaire.
* Vous pouvez maintenant appuyer sur Contrôleur SPL, H pour obtenir de
  l'aide sur la couche Contrôleur SPl.

## Version 17.10

* Si vous utiliser les versions de Windows antérieures à Windows 7 Service
  Pack 1, vous ne pouvez pas basculer au canal de mise à jour de Test Drive
  Fast. Une version future de ce module complémentaire déplacera les
  utilisateurs des anciennes versions de Windows vers un canal de prise en
  charge dédié.
* Plusieurs paramètres généraux tels que le statut de l'annonce en bips, en
  haut et en bas de la notification de playlist et d'autres se trouvent
  maintenant situés dans le nouveau dialogue Paramètres généraux du module
  complémentaire (accessible à partir d'un nouveau bouton dans les
  paramètres du module complémentaire).
* Il est maintenant possible de faire que les options du module
  complémentaire en lecture seule, utilisez uniquement le profil normal, ou
  pas charger les paramètres à partir du disque lorsque Studio
  démarre. Ceux-ci sont contrôlés par de nouveaux commutateurs en ligne de
  commande spécifiques à ce module complémentaire.
* Lors de l'exécution de NVDA depuis le dialogue Exécuter (Windows+R), vous
  pouvez maintenant passer en ligne de commande supplémentaires les
  commutateurs pour modifier la façon dont le module complémentaire
  fonctionne. Ces derniers comprennent "--spl-configvolatile" (paramètres en
  lecture seule), "--spl-configinmemory" (ne pas charger les paramètres du
  disque), et "--spl-normalprofileonly" (utiliser uniquement le profil
  normal).
* Si en sortant de Studio (pas de NVDA) pendant que le changement de profil
  immédiat est actif, NVDA ne donne plus d'annonces trompeurs lors du
  basculement à un changement de profil immédiat lors de l'utilisation de
  Studio à nouveau.

## Version 17.09.1

* À la suite de l'annonce de NV Access, NVDA 2017.3 sera la dernière version
  prise en charge avec les versions de Windows antérieures à  Windows 7
  Service Pack 1, le module complémentaire Studio présentera un message de
  rappel à propos de ça si vous exécuter à partir d'anciennes versions de
  Windows. La fin de la prise en charge des anciennes versions de Windows
  pour ce module complémentaire (via une prise en charge de la version
  long-term) est prévue pour Avril 2018.
* NVDA n'affichera plus de dialogue de démarrage et/ou n'annoncera plus la
  version de Studio si elle a débuté avec un ensemble d'indicateurs minimal
  (nvda -rm). La seule exception est l'ancien dialogue de rappel de version
  de Windows.

## Version 17.09

* Si un utilisateur entre dans le dialogue des options avancées dans les
  paramètres du module complémentaire, le canal et l'intervalle de mise à
  jour ont été définis sur Test Drive Fast et/ou zéro jours, NVDA ne
  présentera plus le message d'avertissement de canal et/ou d'intervalle en
  sortant de ce dialogue.
* Les commandes playlist restante et l'analyse de la durée de piste
  exigeront maintenant le chargement d'une playlist et un message d'erreur
  plus précis sera présenté autrement.

## Version 17.08.1

* NVDA ne sera plus en mesure de laisser Studio jouer la première piste
  lorsqu'un encodeur est connecté.

## Version 17.08

* Changements apportées à la mise à jour des étiquettes du canal : une build
  d'essai est maintenant Test Drive Fast, le canal de développement est Test
  Drive Slow. Les vraies builds "essai" seront réservées aux builds d'essai
  réelles qui nécessitent que les utilisateurs installent manuellement une
  version de test.
* L'intervalle de mise à jour peut maintenant être réglé sur 0 (zéro)
  jours. Cela permet au module complémentaire de vérifier les mises à jour
  lorsque NVDA et/ou SPL Studio démarrent. Une confirmation sera nécessaire
  pour modifier l'intervalle de mise à jour à zéro jours.
* NVDA ne parviendra plus à vérifier les mises à jour du module
  complémentaire si l'intervalle de mise à jour est réglé sur 25 jours ou
  plus.
* Dans les paramètres du module complémentaires, il a été ajouté une case à
  cocher pour laisser NVDA jouer un son lorsque les demandes des auditeurs
  arrivent. Pour l'utiliser complètement, la fenêtre des requêtes doit
  apparaître lorsque les demandes arrivent.
* En appuyant sur la commande de temps de diffusion (NVDA+Maj+F12) deux
  fois, NVDA annoncera les minutes et les secondes restant dans l'heure
  actuelle.
* Il est maintenant possible d'utiliser Chercheur de piste (Control + NVDA +
  F) pour rechercher les noms des pistes que vous avez recherchées avant en
  sélectionnant un terme de recherche à partir d'un historique de termes.
* Lors de l'annonce du titre de la piste actuelle et suivante via
  l'Assistant SPL, il est maintenant possible d'inclure des informations sur
  le lecteur interne de Studio qui jouera la piste (par exemple, le lecteur
  1).
* Ajout d'un paramètre dans les paramètres du module complémentaire sous le
  statut des annonces pour inclure l'information du lecteur lors de
  l'annonce du titre de la piste actuelle et suivante.
* Correction d'un problème dans le caractère indicateur temporaire et
  d'autres dialogues où NVDA n'indiquerait pas de nouvelles valeurs lors de
  la manipulation des horodateurs.
* NVDA peut supprimer l'annonce des titres de colonne tels que l'artiste et
  la catégorie lors de la révision des pistes dans la visionneuse de
  playlist. Il s'agit d'un paramètre spécifique au profil de diffusion.
* Ajouté une case à cocher   dans la boîte de dialogue paramètres du module
  complémentaire pour supprimer l'annonce des titres de colonnes lors de la
  révision des pistes dans la visionneuse de playlist.
* Ajout d'une commande dans la Couche Contrôleur SPL pour annoncer le nom et
  la durée de la piste en cours de lecture de n'importe où (C).
* Lorsque vous obtenez des informations du statut via le Contrôleur SPL (Q)
  pendant l'utilisation de Studio 5.1x, des informations telles que le
  statut du microphone, mode édition chariot et d'autres seront également
  annoncées en plus de la lecture et de l'automatisation.

## Version 17.06

* Vous pouvez maintenant effectuer la commande Recherche de Piste
  (Contrôle+NVDA+F) alors qu'une playlist est chargée mais la première piste
  n'a pas le focus.
* NVDA ne lira plus les tonalités d'erreur ou ne fera rien lors de la
  recherche d'une piste en avant à partir de la dernière piste ou en arrière
  à partir de la première piste, respectivement.
* En appuyant sur NVDA+pavNum Effacement (NVDA+Effacement dans la
  disposition  d'un ordinateur portable), va maintenant annoncer la position
  de la piste suivie du nombre d'éléments dans une playlist.

## Version 17.05.1

* NVDA ne cessera plus d'enregistrer les modifications apportées aux
  paramètres d'alarme à partir de diverses boîtes de dialogue d'alarme (par
  exemple, Alt+NVDA+1 pour l'alarme de fin de piste).

## Version 17.05/15.7-LTS

* L'intervalle de mise à jour peut maintenant être configuré jusqu'à 180
  jours. Pour les installations par défaut, l'intervalle de vérification de
  la mise à jour sera de 30 jours.
* Correction d'un problème où NVDA peut jouer une tonalité d'erreur si
  Studio sort alors qu'un un profil basé sur l'heure est actif.

## Version 17.04

* Ajout d'un support pour le module complémentaire en mode débogage en
  enregistrant diverses informations alors que le module complémentaire est
  actif avec NVDA configuré en Niveau de journalisation : débogage (requiert
  NVDA 2017.1 et versions ultérieures). Pour l'utiliser avec ce module
  complémentaire, après l'installation de NVDA 2017.1, à partir du dialogue
  Quitter NVDA, choisissez l'option "Redémarrer avec le journal activé en
  mode débogage.
* Améliorations apportées à la présentation de diverses boîtes de dialogue
  ajoutées grâce aux fonctionnalités NVDA 2016.4.
* NVDA va télécharger les mises à jour du module complémentaire en
  arrière-plan si vous dites "oui" lorsqu'on lui demande de mettre à jour le
  module complémentaire. Par conséquent, les notifications de téléchargement
  de fichiers depuis les navigateurs Web ne seront plus affichées.
* NVDA ne se bloquera plus lors de la recherche de la mise à jour au
  démarrage en raison du changement du  canal de mise à jour du module
  complémentaire.
* Ajoutée la possibilité d'appuyer sur Contrôle+Alt+touches flèche haut ou
  flèche bas  pour se déplacer entre les pistes  (en particulier, les
  colonnes de piste) verticalement au moment où l'on passe à la rangée
  suivante ou précédente dans un tableau.
* Ajoutée une zone de liste déroulante dans le dialogue paramètres du module
  complémentaire pour définir quelle colonne doit être annoncée lors du
  déplacement vertical des colonnes.
* Déplacement des contrôles fin de piste, intro et alarme microphone depuis
  les paramètres du module complémentaire au nouveau Centre des alarmes.
* Dans Centre des alarmes, les champs d'édition de fin de piste et Piste
  intro sont toujours affichés indépendamment des cases à cocher état de
  notification d'alarme.
* Ajout d'une commande dans Assistant SPL pour obtenir des instantanés de
  playlist tels que le nombre de pistes, la piste la plus longue, les
  meilleurs artistes et ainsi de suite (F8). Vous pouvez également ajouter
  une commande personnalisée pour cette fonction.
* En appuyant une fois sur la commande de geste personnalisé pour les
  instantanés de playlist NVDA peut annoncer et brailler une courte
  information instantanée. En appuyant deux fois sur la commande, NVDA ouvre
  une page Web contenant des informations plus complètes sur les instantanés
  de playlist. Appuyez sur Échap pour fermer cette page Web.
* Suppression du Cadran de piste (version NVDA des touches fléchées
  améliorées), remplacée par les commandes Explorateur de colonnes et
  Navigateur de colonnes/Navigation par tableau). Cela affecte Studio et
  outil de piste.
* Après avoir fermé le dialogue Insérer des pistes pendant qu'un balayage de
  la bibliothèque est en cours, il n'est plus nécessaire d'appuyer sur
  Assistant SPL, Maj+R pour surveiller la progression du balayage.
* Amélioration de la précision de la détection et de l'établissement des
  annonces de la  fin du balayage de la bibliothèque dans Studio 5.10 et
  versions ultérieures. Cela corrige un problème où le moniteur du balayage
  de la bibliothèque se terminera prématurément quand il ya plus de pistes à
  balayer, nécessitant le redémarrage du moniteur du balayage de la
  bibliothèque.
* Amélioration des annonces du statut du balayage de la bibliothèque via le
  contrôleur SPL (Maj+R) en annonçant le comptage de balayage si le balayage
  se produit réellement.
* En mode Démo de studio, lorsque l'écran d'enregistrement s'affiche lors du
  démarrage de Studio, les commandes telles que le temps restant pour une
  piste ne provoqueront plus que NVDA ne fasse rien, lira les tonalités
  d'erreur ou donnera des informations erronées. Un message d'erreur sera
  alors annoncé. Des commandes comme celles-ci nécessiteront que la poignée
  de la fenêtre principale de Studio soit présente.
* Premier support de StationPlaylist Creator.
* Ajout d'une nouvelle commande dans la couche Contrôleur SPL pour annoncer
  le statut de Studio telles que la lecture des pistes et le statut du
  microphone (Q).

## Version 17.03

* NVDA ne semble plus rien faire ou ne lit plus une tonalité d'erreur
  lorsque vous basculer à un profil de diffusion basé sur l'heure.
* Mises à jour des traductions.

## Version 17.01/15.5-LTS

Remarque: 17.01.1/15.5A-LTS remplace la 17.01 en raison des changements
apportés à l'emplacement des nouveaux fichiers du module complémentaire.

* 17.01.1/15.5A-LTS: Modifié à partir duquel les mises à jour sont
  téléchargées pour les versions prises en charges à long
  terme. L'installation de cette version est obligatoire.
* Amélioration de la réactivité et de la fiabilité lors de l'utilisation du
  module complémentaire pour basculer à Studio, en utilisant le focus sur la
  commande Studio à partir d'autres programmes ou lorsqu'un encodeur est
  connecté et NVDA est invité à basculer vers Studio lorsque cela se
  produit. Si Studio est minimisé, la fenêtre Studio s'affichera comme
  indisponible. Dans ce cas, restaurez la fenêtre Studio depuis la barre
  d'état système.
* Si vous modifier des chariots pendant que l'Explorateur de Chariot est
  actif, il n'est plus nécessaire d'entrer à nouveau dans l'Explorateur de
  Chariot pour afficher la mise à jour des assignations de chariot lorsque
  le mode édition chariot est désactivé. Par conséquent, le message pour
  entrer à nouveau dans l'Explorateur de Chariot n'est plus annoncé.
* Dans le module complémentaire 15.5-LTS, correction de la présentation de
  l'interface utilisateur pour le dialogue Paramètres module complémentaire
  SPL.

## Version 16.12.1

* Correction de la présentation de l'interface utilisateur pour le dialogue
  Paramètres module complémentaire SPL.
* Mises à jour des traductions.

## Version 16.12/15.4-LTS

* Plus de travail sur le support Studio 5.20, incluant l'annonce du statut
  en mode insertion chariot (si celui-ci est activé) depuis la couche
  Assistant SPL (T).
* Le basculement du Mode édition/insertion chariot n'est plus affecté par
  les paramètres de type verbosité du message ni par le statut (ce statut
  sera toujours annoncé par la parole et / ou le braille).
* Il n'est plus possible d'ajouter des commentaires aux notes de pause
  temporisées.
* Support pour l'Outil de Piste 5.20, incluant la résolution d'un problème
  où des informations erronées sont annoncées lors de l'utilisation des
  commandes dans l'Explorateur de Colonnes pour annoncer les informations
  sur les colonnes.

## Version 16.11/15.3-LTS

* Premier support de StationPlaylist Studio 5.20, y compris une meilleure
  réactivité lors de l'obtention des informations du statut telles que
  l’automatisation du statut via la couche de l'Assistant SPL.
* Correction des problèmes liés à la recherche de pistes et à l'interaction
  avec celles-ci, y compris l'impossibilité de cocher ou de décocher le
  marqueur de position de piste ou une piste >trouvée via le dialogue
  Recherche de l'intervalle de temps.
* L'ordre d'annonce des colonnes ne revient plus à l'ordre par défaut après
  modification.
* 16.11: Si les profils de diffusion ont des erreurs, la boîte de dialogue
  d'erreur ne cessera plus de s'afficher.

## Version 16.10.1/15.2-LTS

* Vous pouvez maintenant interagir avec la piste qui a été trouvé via la
  Recherche de Piste (Contrôle+NVDA+F) tel que la vérification pour la
  lecture.
* Mises à jour des traductions.

## Version 8.0/16.10/15.0-LTS

La version 8.0 (également connu sous le nom de 16.10) prend en charge la
version SPL Studio 5.10 et ultérieure, avec la 15.0-LTS (anciennement la
7.x) conçu pour fournir de nouvelles fonctionnalités depuis la 8.0 pour les
utilisateurs des versions antérieures de Studio. À moins que dans le cas
contraire les rubriques ci-dessous s’appliquent à les deux, 8.0 et 7.x. Un
dialogue d'avertissement apparaît la première fois que vous utilisez le
module complémentaire 8.0 avec Studio 5.0x installé, vous demandant
d’utiliser la version  15.x LTS.

* Le Schéma de la version a changé pour refléter la version year.month au
  lieu de major.minor. Au cours de la période de transition (jusqu'au
  mi-2017), la version 8.0 est synonyme de la version 16.10, avec la 7.x LTS
  étant désigné la 15.0 en raison des changements incompatibles.
* Le code source du module complémentaire est désormais hébergé sur GitHub
  (référentiel  localisé à https://github.com/josephsl/stationPlaylist).
* Ajouter un dialogue de Bienvenue qui se lance au démarrage de Studio après
  l’installation du module complémentaire. Une commande (NVDA+AltF1) a été
  ajoutée pour rouvrir ce dialogue une fois rejeté.
* Changements de diverses commandes du module complémentaire, y compris la
  suppression du basculement des annonces des statut (Contrôle+NVDA+1),
  réassigné Alarme de fin de piste à Alt+NVDA+1, basculement  de
  l'Explorateur de Chariot  est maintenant Alt+NVDA+3, le dialogue alarme
  microphone est Alt+NVDA+4 et le dialogue Paramètres du module
  complémentaire/encodeur est Alt+NVDA+0. Cela a été fait pour permettre
  d'être Assigner  à Contrôle+NVDA+rangée de numéro à l'Explorateur de
  Colonnes.
* 8.0: Relâché la restriction de l'Explorateur de colonnes à la place dans
  la  7.x donc les  chiffres 1 jusq'à 6 peuvent être configurés pour
  annoncer les colonnes dans Studio 5.1x.
* 8.0: La commande  pour le basculement du Cadran de piste et  les paramètre
  correspondant dans les paramètres du module complémentaire sont obsolètes
  et seront supprimées dans la 9.0. Cette commande restent disponible dans
  le module complémentaire 7.x.
* Ajouté Contrôle+Alt+début/fin pour déplacer le Navigateur de Colonne à la
  première ou la dernière colonne dans la Visionneuse de playlist.
* Vous pouvez maintenant ajouter, afficher, modifier ou supprimer les
  commentaires (notes) de la piste. Appuyer sur Alt+NVDA+C depuis une piste
  dans la visionneuse de playlist pour entendre les commentaires si défini,
  appuyez deux fois pour copier le commentaire dans le presse-papiers  ou
  trois fois pour ouvrir un dialogue pour modifier les commentaires.
* Ajoutée la possibilité d'annoncer si un commentaire de piste existe,ainsi
  que d’un paramètre dans les paramètres du module complémentaire pour
  contrôler comment cela devrait être fait.
* Ajouter un nouveau paramètre dans le dialogue paramètres du module
  complémentaire pour permettre a NVDA de vous notifier si vous avez atteint
  le haut ou le bas de la visionneuse de playlist.
* Lors de la réinitialisation des paramètres du module complémentaire, vous
  pouvez maintenant spécifier quel type de restauration vous souhaitez
  avoir. Par défaut, les paramètres du module complémentaire seront
  réinitialisés, avec des cases à cocher pour la réinitialisation des
  changement de profil immédiat, pofil basé sur l'heure, paramètres de
  l’encodeur et les commandes pour effacer la piste ajouté pour
  réinitialiser la boîte de dialogue Paramètres.
* Dans l'Outil de piste, vous pouvez obtenir des informations sur l'album et
  le code du CD en appuyant sur Contrôle+NVDA+9 et Contrôle+NVDA+0,
  respectivement.
* Amélioration des performances lors de l’obtention des informations de
  colonne pour la première fois dans l'Outil de Piste.
* 8.0: Ajouté un dialogue dans les paramètres du module complémentaire pour
  configurer les tranches de l'Explorateur de Colonnes pour l'Outil de
  Piste.
* Vous pouvez maintenant configurer l'intervalle alarme microphone depuis le
  dialogue Alarme microphone (Alt+NVDA+4).

## Version 7.5/16.09

* NVDA n'affichera plus la fenêtre de la boîte de dialogue de la progression
  de la mise à jour si le canal de mise à jour du module complémentaire
  vient de changer.
* NVDA honorera le canal de mise à jour sélectionnée lors du téléchargement
  des mises à jour.
* Mises à jour des traductions.

## Version 7.4/16.08

Version 7.4 est également connu comme 16.08 selon le numéro de version
year.month pour les publications stable.

* Il est possible de sélectionner le canal de mise à jour du module
  complémentaire depuis les paramètres du module complémentaire/Options
  avancées pour être supprimé plus tard en 2017. Pour 7.4, les canaux
  disponibles sont bêta, stable et long-terme.
* Ajouté un paramètre dans les paramètres du module complémentaire/Options
  avancées pour configurer l'intervalle de recherche de mise à jour entre 1
  et 30 jours (par défaut est 7 ou recherches hebdomadaire).
* La commande pour le Contrôleur SPL et la commande pour la mise en focus de
  Studio ne sera pas disponibles à partir des écrans sécurisés.
* Nouvelles et mises à jour des traductions et l'ajout de documentation
  localisé en plusieurs langues.

## Changements pour la version 7.3

* Amélioration des performances légère quand on regarde les informations
  telles que l’automatisation via certaines commandes de l'Assistant SPL.
* Mises à jour des traductions.

## Changements pour la version 7.2

* En raison de la suppression du format de l'ancien style de configuration
  interne, il est obligatoire d'installer le module complémentaire 7.2. Une
  fois installé, vous ne pouvez pas revenir à une version antérieure du
  module complémentaire.
* Ajout d'une commande dans le Contrôleur SPL pour annoncer le nombre
  d'auditeurs (I).
* Vous pouvez maintenant ouvrir le dialogue Paramètres module complémentaire
  SPL et le dialogue Paramètres de l'encodeur en appuyant sur
  Alt+NVDA+0. Vous pouvez toujours utiliser Contrôle+NVDA+0 pour ouvrir ces
  boîtes de dialogue (pour être supprimé dans le module complémentaire 8.0).
* Dans l'Outil de Piste, vous pouvez utiliser Contrôle+Alt+les touches
  flèche gauche ou flèche droite pour naviguer entre les colonnes.
* Contenu de diverses boîtes de dialogue de Studio comme la boîte de
  dialogue À propos dans Studio 5.1x sont maintenant annoncées.
* Dans l'Encodeur SPL NVDA fera arrêter la tonalité de connexion si la
  connexion automatique est activée, et puis désactivée depuis le menu
  contextuel alors que l’encodeur sélectionné se connecte.
* Mises à jour des traductions.

## Changements pour la version 7.1

* Correction des erreurs rencontrés lors de la mise à niveau depuis le
  module complémentaire 5.5 et en dessous de la 7.0.
* Lorsque vous répondez "non" lors de la réinitialisation des paramètres du
  module complémentaire, vous retourné à la boîte de dialogue Paramètres
  module complémentaire et NVDA se souviendra du paramètre changement de
  profil immédiat.
* NVDA vous demandera de reconfigurer les étiquettes de flux et d’autres
  options de l'encodeur si le fichier de configuration de l'encodeur est
  endommagé.

## Changements pour la version 7.0

* Ajouté la fonction Rechercher une mise à jour du module
  complémentaire. Cela peut se faire manuellement (Assistant SPL,
  Contrôle+Maj+U) ou automatiquement (configurable depuis la boîte de
  dialogue Options avancées dans la boîte de dialogue paramètres du module
  complémentaire).
* Il n'est plus nécessaire de rester dans la fenêtre de la visionneuse de
  playlist afin d'invoquer la plupart des commandes couche Assistant SPL ou
  obtenir des annonces de temps tels que le temps restant pour la piste et
  le temps de diffusion.
* Changements des commandes Assistant SPL, y compris Durée de la playlist
  (D), réassignation de durée de sélection de l'heure de Maj+H à Maj+S et
  Maj+H maintenant utilisé pour annoncer la Durée des pistes restantes pour
  la tranche horaire courante, la commande Statut de Métadonnées en
  streaming réassignée (1 jusqu'à 4, 0 est maintenant Maj+1 jusqu'à Maj+4,
  Maj+0).
* Il est maintenant possible d'invoquer Recherche de piste via l'Assistant
  SPL (F).
* Assistant SPL, chiffres 1 jusqu'à 0 (6 pour Studio 5.01 ou version
  antérieure) peut être utilisé pour annoncer les informations d'une colonne
  spécifique. Ces tranches de colonne peuvent être modifiés sous l'élément
  Explorateur de Colonnes dans la boîte de dialogue Paramètres module
  complémentaire.
* Corrigé les nombreuses erreurs signalées par les utilisateurs lors de
  l'installation du module complémentaire 7.0 pour la première fois lorsque
  aucune version antérieure de ce module complémentaire a été installé.
* Améliorations apportées au Cadran de Piste, y compris la meilleure
  réactivité lors d’un déplacement dans les colonnes et le suivi de comment
  les colonnes sont présentées à l'écran.
* Ajoutée la possibilité d'appuyer sur Contrôle+Alt+touches flèche gauche ou
  flèche droite pour se déplacer entre les colonnes de piste.
* Il est maintenant possible d'utiliser une commande différente   pour la
  disposition du lecteur d'écran pour les commandes Assistant SPL. Aller
  dans la boîte de dialogue Options avancées depuis Paramètres module
  complémentaire pour configurer cette option entre les dispositions NVDA,
  JAWS et Window-Eyes. Voir les commandes Assistant SPL ci-dessus pour plus
  de détails.
* NVDA peut être configuré pour basculer vers un profil de diffusion
  spécifique à un jour et à une heure spécifier. Utiliser la nouvelle boîte
  de dialogue Déclencheurs dans Paramètres module complémentaire pour
  configurer cela.
* NVDA annoncera le nom du profil lors du basculement vers via le changement
  immédiat (Assistant SPL, F12) ou comme un résultat du profil basé sur
  l'heure lequel devient actif.
* Déplacé la bascule du changement immédiat(maintenant une case à cocher)
  vers la nouvelle boîte de dialogue Déclencheurs.
* Entrées dans la liste déroulante des profils dans la boîte de dialogue
  Paramètres module complémentaire maintenant s'affiche le drapeaux du
  profil par exemple actif, que ce soit un changement de profil immédiat et
  ainsi de suite.
* Si un problème sérieux avec le fichier lors de la lecture du profil de
  diffusion on été trouvés, NVDA présentera une boîte de dialogue d'erreur
  et va réinitialiser les paramètres par défaut au lieu de ne rien faire ou
  donnera une tonalité d'erreur.
* Les paramètres seront sauvegardés sur le disque si et seulement si vous
  modifiez les paramètres. Ceci prolonge la vie des SSD (solid state drives(
  en empêchant les arrêts inutiles sur le disque si aucun paramètres n’ont
  été modifiés.
* Dans le dialogue paramètres du module complémentaire les contrôles
  utilisés pour basculer l'annonce de l'heure prévue, le nombre d'auditeurs,
  le nom du chariot et le nom de la piste a été déplacé vers un dialogue
  Annonces des statut (sélectionnez  le bouton annonce de statut pour ouvrir
  cette boîte de dialogue).
* Ajouter un nouveau paramètre dans le dialogue paramètres du module
  complémentaire pour permettre a NVDA de jouer un bip pour les différentes
  catégories de piste lors du déplacement entre les pistes dans la
  visionneuse de playlist.
* Tentative lors de l'ouverture de l'option de configuration de métadonnées
  dans le dialogue de paramètres du module complémentaire alors que le
  dialogue rapide de métadonnées en streaming est ouvert ne provoquera plus
  que NVDA ne puisse rien faire ou de jouer une tonalité d’erreur. NVDA va
  maintenant vous demander de fermer le dialogue de métadonnées en streaming
  avant que vous puissiez ouvrir les paramètres du module complémentaire.
* En annonçant le temps comme le temps restant pour la piste en cours de
  lecture, les heures sont également annoncées. Par conséquent, le réglage
  pour l'annonce des heures est activé par défaut.
* Appuyant sur le Contrôleur SPL, R permet maintenant a NVDA d’annoncer le
  temps restant en heures, minutes et secondes (minutes et secondes s’il
  s’agit d’un tel cas).
* Dans les encodeurs, en appuyant sur contrôle + NVDA + 0 se présentera le
  dialogue Paramètres de l'encodeur permettant de configurer différentes
  options telles que l'étiquette de flux, en plaçant le focus à Studio
  lorsqu'il est connecté et ainsi de suite.
* Dans les encodeurs, il est maintenant possible de désactiver la tonalité
  de progression de connexion (configurable à partir  de la boîte  de
  dialogue paramètres de l'encodeur).

## Changements pour la version 6.4

* Correction d'un problème majeur lors du retour au basculement d'un profil
  à partir d'un changement de profil immédiat et d'un changement de profil
  immédiat devenue active à nouveau, vu après la suppression d'un profil qui
  a été positionné juste avant le profil précédemment actif. Lorsque vous
  essayez de supprimer un profil, une boîte de dialogue d'avertissement
  s'affichera si un changement de profil immédiat est actif.

## Changements pour la version 6.3

* Améliorations de la sécurité interne.
* Lorsque le module complémentaire 6.3 ou version ultérieure est tout
  d'abord lancé sur un ordinateur fonctionnant sous Windows 8 ou supérieur
  avec NVDA 2016.1 ou installé par la suite, un dialogue d'alerte
  s'affichera vous demandant pour désactiver le Mode d'atténuation audio
  (NVDA+Maj+D). Sélectionnez la case à cocher pour supprimer cette boîte de
  dialogue à l'avenir.
* Ajouté une commande pour envoyer des rapports de bugs, des suggestions de
  fonctionnalité et autres commentaires aux développeurs du module
  complémentaire (Contrôle+NVDA+tiret (trait d'union, "-")).
* Mises à jour des traductions.

## Changements pour la version 6.2

* Correction d'un problème avec la commande reste de la playlist (Assistant
  SPL, D (R si le mode de compatibilité est activé)) lorsque la durée de
  l'heure actuelle a été annoncée par opposition à la playlist entière (le
  comportement de cette commande peut être configuré à partir des Paramètres
  Avancés dans la boîte de dialogue Paramètres du module complémentaire).
* NVDA peut maintenant annoncer le nom de la piste en cours de lecture tout
  en utilisant un autre programme (configurable depuis les paramètres du
  module complémentaire).
* Le paramètre utilisé pour laisser la commande Contrôleur SPL pour appeler
  l'Assistant SPL est maintenant honoré (auparavant elle a été activée en
  permanence).
* Dans les encodeurs SAM, les commandes Contrôle+F9 et Contrôle+F10
  fonctionne maintenant correctement.
* Dans les encodeurs, lorsqu'un encodeur est mis en focus tout d'abord et si
  cet encodeur est configuré pour contrôler en arrière-plan, NVDA va
  maintenant démarrer le contrôle en arrière-plan automatiquement.

## Changements pour la version 6.1

* L'ordre des colonnes annoncer et inclusion, ainsi que les paramètres de
  métadonnées en streaming sont maintenant des paramètres spécifiques au
  profil.
* Lors du changement de profils, les flux de métadonnées correct seront
  activées.
* Lors de l'ouverture de la boîte de dialogue paramètres rapide de
  métadonnées en streaming (commande non assignée), les paramètres modifiés
  sont maintenant appliqués au profil actif.
* Lors du démarrage de Studio, changé la façon dont les erreurs s'affichent
  si le seul profil corrompu est le profil normal.
* Lorsque vous modifiez certains paramètres à l'aide de raccourcis clavier
  tels que  les annonces de statut, corrigé un problème où les paramètres
  modifiés ne sont pas conservées lors du basculement vers et depuis un
  changement de profil  immédiat.
* Lorsque vous utilisez une commande Assistant SPL avec un geste
  personnalisé défini (tel que  la commande piste suivante), il n'est plus
  nécessaire de rester dans la visionneuse de playlist de Studio pour
  utiliser ces commandes (ils peuvent être effectuées depuis les autres
  fenêtres de Studio).

## Changements pour la version 6.0

* Nouvelles commandes de l'Assistant SPL, y compris annonçant le titre de la
  piste en cours de lecture (C), annonçant le statut des métadonnées en
  streaming (E, 1 jusqu'à 4 et 0) et l'ouverture du guide de l'utilisateur
  en ligne (Maj+F1).
* La possibilité de mmettre en bloc les paramètres favoris comme les profils
  de diffusion à utiliser lors d'une présentation et de basculer à un profil
  prédéfini. Consultez le guide du module complémentaire pour plus de
  détails sur les profils de diffusion.
* Ajouté un nouveau paramètre dans les paramètres du module complémentaire
  pour contrôler la verbosité du message (certains messages seront
  raccourcies lorsque la verbosité avancée est sélectionnée).
* Ajouté un nouveau paramètre dans les paramètres du module complémentaire
  pour laisser à NVDA annoncer les heures, minutes et secondes pour les
  commandes de durée de piste ou playlist  (caractéristiques affectée y
  compris annonçant le temps écoulé et restant de la piste en cours de
  lecture, l'analyse de durée de piste et d'autres).
* Vous pouvez maintenant demander à NVDA d'indiquer la longueur totale d'un
  intervalle des pistes  via la fonctionnalité d'analyse de durée de
  piste. Appuyer sur AssistantSPL, F9 pour marquer la piste en cours comme
  marqueur de début, se déplacer à la fin de l'intervalle de piste et
  appuyez sur Assistant SPL, F10. Ces commandes peuvent être réassignées
  donc on n'a pas à invoquer la couche Assistant SPL pour effectuer
  l'analyse de durée de piste.
* Ajouté une boîte de dialogue Recherche de colonne (commande non assignée)
  pour rechercher du texte dans des colonnes spécifiques tels que l'artiste
  ou une partie du nom du fichier.
* Ajouté la boîte de dialogue Recherche de l'intervalle de temps (commande
  non assignée) pour trouver une piste avec une durée qui se situe dans un
  intervalle spécifié, utile si je souhaite trouver une piste pour remplir
  une tranche horaire.
* Ajouté la possibilité de réorganiser l'annonce de la piste en colonne et
  pour supprimer l'annonce d'une  colonnes spécifiques si "utiliser l'ordre
  affichés sur l'écran" est non coché depuis la boîte de dialogue paramètres
  du module complémentaire. Utiliser la boîte de dialogue "Gérer les
  annonces de colonne" pour réorganiser les colonnes.
* Ajouté une boîte de dialogue (commande non assignée) pour basculer
  rapidement entre activer/désactiver des métadonnées en streaming.
* Ajouté un paramètre dans les paramètres du module complémentaire pour
  configurer lorsque le statut des métadonnées en streaming devraient être
  annoncée et pour activer des métadonnées en streaming.
* Ajouté la possibilité de marquer une piste comme un marqueur de position
  afin d'y revenir plus tard (Assistant SPL, Contrôle+K pour définir,
  Assistant SPL, K pour ce déplacer à la piste marquée).
* Amélioration des performances lorsque vous rechercher le texte sur la
  piste suivante ou précédente contenant le texte recherché.
* Ajouté un paramètre dans les paramètres du module complémentaire pour
  configurer la notification d'alarme (bip, message ou tous les deux).
* Il est maintenant possible de configurer l'alarme du microphone entre 0
  désactivé) et deux heures (7200 secondes) et d'utiliser les touches flèche
  haut et bas pour configurer ce paramètre.
* Ajouté un paramètre dans les paramètres du module complémentaire pour
  permettre une notification du microphone actif afin de le recevoir
  périodiquement.
* Vous pouvez maintenant utiliser la commande à bascule pour le Cadran de
  Piste en Studio pour  basculer le Cadran de Piste dans l'Outil de Piste
  sous réserve que vous n'assignez une commande pour basculer le Cadran de
  Piste dans l'Outil de Piste.
* Ajouté la possibilité d'utiliser la commande Couche Contrôleur SPL pour
  appeler la Couche de l'Assistant SPL (configurable depuis la boîte de
  dialogue paramètres avancé trouvé dans la boîte de dialogue paramètres du
  module complémentaire).
* Ajouté la possibilité pour NVDA d'utiliser certaines commandes de
  l'Assistant SPL utilisés par les autres lecteurs d'écran. Pour ce faire,
  allez dans les paramètres du module complémentaire, sélectionnez
  Paramètres Avancés et cochez la case à cocher mode compatibilité lecteur
  écran.
* Dans les encodeurs, les paramètres tels que la mise en focus de Studio
  lorsqu'il est connecté sont maintenant rappeler.
* Il est maintenant possible d'afficher plusieurs colonnes depuis la fenêtre
  de l'encodeur (tels que le statut de la connexion de l'encodeur) via
  Contrôle+NVDA+chiffre de la commande ; consulter les commandes de
  l'encodeur ci-dessus.
* Correction d'un bug rare où lors du basculement à Studio ou lors de la
  fermeture d'une boîte de dialogue NVDA ((y compris les boîtes de dialogue
  du module complémentaire Studio) d'empêché les commandes de piste (comme
  le basculement du Cadran de Piste) de fonctionner comme prévu.

## Changements pour la version 5.6

* Dans Studio 5.10 et versions ultérieures, NVDA n'annonce plus "non
  sélectionné" lorsque joue la  piste sélectionnée.
* Suite à un problème avec Studio lui-même, NVDA maintenant annoncera le nom
  de la piste en cours de lecture automatiquement. Une option pour
  activer/désactiver ce comportement a été ajoutée dans la boîte de dialogue
  paramètres du module complémentaire Studio.

## Changements pour la version 5.5

* Jouer après la configuration de la connexion se souviendra lors du
  déplacement en dehors de la fenêtre de l'encodeur.

## Changements pour la version 5.4

* En exécutant le balayage de la bibliothèque depuis la boîte de dialogue
  Insérer des pistes n'entraîne plus à NVDA de ne pas annoncer le statut du
  balayage ou jouer des tonalités d'erreur si NVDA est configuré pour
  annoncer l'avancement du balayage de la bibliothèque ou le nombre de
  balayages.
* Mises à jour des traductions.

## Changements pour la version 5.3

* La correction du bogue faisant que l'Encodeur SAM (ne lisait pas la piste
  suivante si une piste est en cours de lecture et lorsque l'encodeur se
  connecte), est maintenant disponible pour les utilisateurs de l'encodeur
  SPL.
* NVDA n'affiche plus d'erreurs et ne manque plus de réagir quand, dans
  l'assistant de SPL, F1, (Dialogue de l'aide de l'assistant) est actionnée.

## Changements pour la version 5.2

* NVDA ne permettra plus à ces deux boîtes de dialogue paramètres et alarme
  d'être ouverte. Un avertissement apparaît vous demandant de fermer la
  boîte de dialogue ouverte préalablement avant d'ouvrir une autre boîte de
  dialogue.
* Lors du contrôle d'un ou plusieurs encodeurs en appuyant sur le Contrôleur
  SPL, E annoncera maintenant le nombre d'encodeur, l'ID de l'encodeur et
  l'étiquette(s) de flux dans le cas échéant.
* NVDA supporte toutes les commandes connecter/déconnecter
  (Contrôle+F9/Contrôle+F10) dans les encodeurs SAM.
* NVDA ne  lira plus la piste suivante si un encodeur se connecte alors que
  Studio est entrain de lire une piste et Studio on lui dit de lire les
  pistes lorsqu'un encodeur est connecté.
* Mises à jour des traductions.

## Changements pour la version 5.1

* Il est maintenant possible de visualiser les colonnes individuelles dans
  l'Outil de piste via le Cadran  de piste (touche de basculement non
  assigné). Note ce Studio doit être activée avant d'utiliser ce mode.
* Ajouté une case à cocher   dans la boîte de dialogue paramètres du module
  complémentaire Studio pour basculer entre activer/désactiver l'annonce du
  nom du chariot en cours de lecture.
* Le basculement du microphone entre  activer/désactiver via le contrôleur
  SPL n'entraîne plus de tonalités d'erreur afin d'être lu ou basculer entre
  activer/désactiver le son pour ne pas être lu.
* Si une commande personnalisée est assignée pour une commande couche
  Assistant SPL et cette commande est appuyée correctement après d'avoir
  entré dans l'Assistant SPL, NVDA maintenant, va rapidement quitter
  l'Assistant SPL.

## Changements pour la version 5.0

* Une boîte de dialogue de configuration dédié pour le module complémentaire
  SPL a été ajoutée, accessible depuis le menu préférences de NVDA ou en
  appuyant sur Contrôle+NVDA+0 depuis la fenêtre SPL.
* Ajouté la possibilité de réinitialiser tous les paramètres aux valeurs par
  défaut via la boîte de dialogue configuration.
* Si certains des paramètres ont des erreurs, seul les paramètres concernés
  seront réinitialisés aux valeurs par défaut.
* Ajouté un Mode écran tactile dédié à SPL et des commandes tactile pour
  exécuter diverses commandes Studio.
* Changements de couche Assistant SPL incluent l'ajout de la commande aide
  couche (F1) et suppression des commandes pour alterner entre
  activer/désactiver nombre d'auditeurs (Maj+I) et anonce du temps planifier
  (Maj+S). Vous pouvez configurer ces paramètres dans la boîte de dialogue
  paramètres du module complémentaire.
* Renommé "bascule  entre activé/désactivé l'annonce" à "l'annonce de
  statut" comme les bips sont utilisés pour annoncer les autres informations
  de statut comme l'exécution du balayage de la bibliothèque.
* Le paramètre pour l'annonce de statut est maintenant conservé dans les
  sessions. Auparavant, vous deviez configurer ce paramètre manuellement au
  démarrage de Studio.
* Vous pouvez maintenant utiliser la fonction Cadran de piste pour
  visualiser les colonnes dans une entrée de piste dans la visionneuse de
  playlist principale du Studio (pour basculer entre activer/désactiver
  cette fonction, appuyez sur la commande que vous avez assigné pour cette
  fonctionnalité).
* Vous pouvez maintenant assigner des commandes personnalisées pour écouter
  les informations de température ou pour annoncer le titre de la piste à
  venir si planifié.
* Ajouté une case à cocher dans la boîte de dialogue fin de piste et allarme
  chanson intro pour activer ou désactiver ces alarmes (cocher pour
  activer). Ceux-ci peuvent également être "configurée" depuis les
  paramètres du module complémentaire.
* Correction d'un problème où en appuyant sur la boîte de dialogue alarme ou
  sur les commandes  du chercheur de piste alors qu'une autre alarme ou la
  boîte de dialogue trouver est ouverte entraînerait qu'une autre instance
  de la même boîte de dialogue apparaisse. NVDA affichera un message vous
  demandant tout d'abord de fermer la boîte de dialogue préalablement
  ouverte.
* Changements et corrections  dans l'explorateur de chariot, y compris en
  explorant les  banques de chariot incorrect Lorsque l'utilisateur n'a pas
  le focus sur la visionneuse de playlist. L'explorateur de chariot va
  maintenant vérifiez que vous êtes dans la visionneuse de playlist.
* Ajouté la possibilité d'utiliser la commande Couche Contrôleur SPL pour
  appeler Assistant SPL (expérimental ; consulter le guide du module
  complémentaire sur la façon d'activer ceci).
* Dans les fenêtres de l'encodeur, la commande pour annoncer la date et
  l'heure de NVDA (NVDA+F12 par défaut) annoncera l'heure y compris en
  secondes.
* Vous pouvez maintenant contrôler différents encodeurs pour le statut de la
  connexion et pour les autres messages en appuyant sur Contrôle+F11 alors
  que l'encodeur que vous souhaitez contrôler a le focus (fonctionne mieux
  lorsque vous utilisez des encodeurs  SAM).
* Ajout d'une commande dans la couche Contrôleur SPL pour annoncer le statut
  des encodeurs étant contrôlés (E).
* Une solution de contournement est maintenant disponible pour corriger un
  problème où NVDA annonçait les étiquettes de flux pour les encodeurs
  incorrects, surtout après la suppression d'un encodeur (pour réaligner
  les étiquettes de flux, appuyez sur Contrôle+F12, puis sélectionnez la
  position de l'encodeur, que vous avez supprimé).

## Anciennes versions

S'il vous plaît voir le lien changelog pour les notes de version  pour les
anciennes versions du modules complémentaire.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: http://www.josephsl.net/files/nvdaaddons/getupdate.php?file=spl-lts16

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
