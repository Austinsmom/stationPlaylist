# StationPlaylist Studio #

* Autores: Geoff Shang, Joseph Lee y otros colaboradores
* Descargar [Versión estable][1]
* Descargar [versión de desarrollo][2]

Este paquete de complementos proporciona una utilización mejorada de Station
Playlist Studio, así como utilidades para controlar el Studio desde
cualquier lugar.

Para más información acerca del complemento, lee la [guía del
complemento][4]. Para los desarrolladores que busquen cómo compilar el
complemento, consulta buildInstructions.txt localizado en la raíz del
repositorio del código fuente del complemento.

NOTAS IMPORTANTES:

* Este complemento requiere de NVDA 2017.4 o posterior y StationPlaylist
  Studio 5.10 o posterior.
* Si utilizas Windows 8 o posterior, para una mejor experiencia, deshabilita
  el modo atenuación de audio.
* El complemento 8.0/16.10 requiere de Studio 5.10 o posterior. Para
  retransmisores que utilicen Studio 5.0x y/o Windows XP, Vista o 7 sin
  Service Pack 1, está disponible una versión de soporte extendido
  (15.x). La última versión estable para soportar versiones de Windows
  anteriores a 7 Service Pack 1 es 17.11.2.
* A partir de 2018, los registros de cambios para versiones antiguas se
  encontrarán en GitHub. Este readme del complemento listará cambios desde
  la versión 5.0 (2015 onwards).
* Ciertas características del complemento (especialmente la actualización)
  no funcionarán bajo algunas condiciones, incluyendo la ejecución de NVDA
  en modo seguro.
* Debido a limitaciones técnicas, no puedes instalar ni utilizar este
  complemento en la versión de Windows Store de NVDA.

## Teclas de atajo

* Alt+Shift+T desde la ventana de Studio: anuncia el tiempo transcurrido
  para la pista actual en reproducción.
* Control+Alt+T (deslizar  con dos dedos hacia abajo en modo táctil para
  SPL) desde la ventana de Studio: anuncia el tiempo restante para la pista
  que se esté reproduciendo.
* NVDA+Shift+F12 (deslizar  con dos dedos hacia arriba en modo táctil para
  SPL) desde la ventana Studio: anuncia el tiempo de emisión tal como 5
  minutos para el principio de la hora. Pulsando esta orden dos veces
  anunciará los minutos y segundos hasta la hora.
* Alt+NVDA+1 (deslizar dos dedos a la derecha en modo SPL) desde la ventana
  de Studio: abre el diálogo de opciones de fin de pista.
* Alt+NVDA+2 (deslizar  con dos dedos hacia a la izquierda en modo táctil
  para SPL) desde la ventana Studio: Abre el diálogo de configuración de
  alarma de intro de la canción.
* Alt+NVDA+3 desde la ventana Studio: activa o desactiva el explorador de
  cart para aprender las asignaciones de cart.
* Alt+NVDA+4 desde la ventana Studio: Abre el diálogo alarma del micrófono.
* Control+NVDA+f desde la ventana del Studio: Abre un diálogo para encontrar
  una pista sobre la base del artista o del nombre de la canción. Pulsa
  NVDA+F3 para encontrar hacia adelante o NVDA+Shift+F3 para encontrar hacia
  atrás.
* Alt+NVDA+R desde la ventana de Studio: Pasos de las opciones de anunciado
  del escaneado de biblioteca.
* Control+Shift+X desde la ventana de Studio: Pasos de las opciones del
  temporizador braille.
* Control+Alt+flecha derecha o izquierda (mientras se enfoca una pista):
  anuncia la columna de la pista siguiente o anterior.
* Control+Alt+flecha abajo/arriba (mientras se enfoque una pista): Mueven a
  la pista siguiente o anterior y anuncian columnas específicas (no
  disponible en el complemento 15.x).
* control+NVDA+1 hasta 0 (6 para Studio 5.0x): anuncia el contenido de la
  columna para una columna específica.
* Alt+NVDA+C mientras se enfoca una pista: anuncia los comentarios de pista
  si los hay.
* Alt+NVDA+0 desde la ventana Studio: abre el diálogo de configuración del
  complemento para Studio.
* Control+NVDA+- (guión) desde la ventana de Studio: envía retroalimentación
  al desarrollador del complemento utilizando el cliente de correo
  predeterminado.
* Alt+NVDA+F1: abre el diálogo de bienvenida.

## Órdenes sin asignar

Las siguientes órdenes no se asignaron de manera predeterminada; si deseas
asignnarlas, utiliza el diálogo Gestos de Entrada para añadir órdenes
personalizadas.

* Cambia a la ventana SPL Studio desde cualquier programa.
* SPL Controller layer.
* Anunciar el estado de Studio tal como reproducción de pista desde otros
  programas.
* Capa SPL Assistant desde SPL Studio.
* Anuncia el tiempo incluyendo segundos desde SPL Studio.
* Anuncia la temperatura.
* Anuncia el título de la siguiente pista si se programó.
* Annuncia el título de la pista actualmente en reproducción.
* Marcando pista actual para comenzar el análisisx de tiempo de pista.
* Realizando análisis de tiempo de pista.
* Tomar instantáneas de la lista de reproducción.
* Encontrar texto en columnas específicas.
* Encontrar pista con duración que caiga dentro de un rango dado a través de
  buscador de rango de tiempo.
* Habilitar o deshabilitar cíclicamente metadatos del streaming.

## Órdenes adicionales al utilizar los codificadores Sam o SPL 

Las siguientes órdenes  están disponibles al utilizar los codificadores Sam
o SPL :

* F9: conecta a un servidor de streaming.
* F10: (Sólo SAM encoder): Desconecta de un servidor de streaming.
* Control+F9/Control+F10 (sólo codificador SAM): Conecta o desconecta todos
  los codificadores.
* F11: Activa o desactiva si NVDA cambiará a la ventana Studio para el
  codificador seleccionador si está conectado.
* Shift+F11: conmuta si Studio reproducirá la primera pista seleccionada
  cuando el codificador esté conectado a un servidor de streaming.
* Control+F11: Conmuta el monitoreo de fondo del codificador seleccionado.
* F12: Abre un diálogo para introducir etiquetas personalizadas para el
  codificador o el stream seleccionado.
* Control+F12: abre un diálogo para seleccionar el codificador que has
  eliminado (para realinear las etiquetas de cadena y las opciones del
  codificador).
* Alt+NVDA+0: abre el diálogo opciones del codificador para configurar
  opciones tales como etiqueta de cadena.

Además, las órdenes de revisión de columna están disponibles, incluyendo:

* Control+NVDA+1: posición del codificador.
* Control+NVDA+2: etiqueta de cadena.
* Control+NVDA+3 desde el codificador SAM: formato del codificador.
* Control+NVDA+3 desde el codificador SPL : Opciones del codificador.
* Control+NVDA+4 desde el codificador SAM: estado de conexión del
  codificador.
* Control+NVDA+4 desde el codificador SPL: velocidad de transferencia o
  estado de la conexión.
* Control+NVDA+5 desde el codificador SAM: descripción del Estado de la
  conexión.

## Capa de SPL Assistant

Este conjunto de capas de órdenes te permite obtener varios estados enSPL
Studio, tales como si se está escuchando una canción, duración total de
todas las pistas para la hora y así sucesivamente. desde la ventana SPL
Studio, pulsa la orden de capa SPL Assistant,  luego pulsa una de las teclas
de la siguiente lista (una o más órdenes son exclusivas para el visualizador
de lista de reproducción). También puedes configurar NVDA para emular
órdenes desde otros lectores de pantalla.

Las órdenes disponibles son:

* A: Automatización.
* C (Shift+C en distribuciones JAWS y Window-Eyes): Título para la pista
  actualmente en reproducción.
* C (distribuciones JAWS y Window-Eyes): conmuta el explorador de cart
  (visualizador de lista de reproducción sólo).
* D (R en distribución JAWS): duración restante para la lista de
  reproducción (si se da un mensaje de error, se mueve al visualizador de
  lista de reproducción y entonces emite esta orden).
* E(G en distribución Window-Eyes): estado de metadatos del streaming.
* Shift+1 hasta Shift+4, Shift+0: estado para los metadatos individuales de
  la URL del streaming (0 es para el codificador DSP).
* E (distribución Window-Eyes): tiempo transcurrido para la pista
  actualmente en reproducción.
* F: busca pista (visualizador de lista de reproducción sólo).
* H: Duración de la música para el actual espacio de tiempo.
* Shift+H: duración restante de la pista o del slot horario.
* I (L en distribuciones JAWS y Window-eyes): cuenta de oyentes.
* K: se mueve a la pista marcada (sólo visualizador de lista de
  reproducción).
* Control+K: pone la pista actual como la pista marcada (sólo visualizador
  de lista de reproducción).
* L (Shift+L en las distribuciones JAWS y Window-Eyes): línea auxiliar.
* M: Micrófono.
* N: Título para la siguiente pista programada.
* P: Estado de reproducción (reproduciendo o detenido).
* Shift+P: Tono de la pista actual.
* R (Shift+E en disbribuciones JAWS y Window_eyes): Grabar en archivo
  habilitado/deshabilitado.
* Shift+R: Monitor de escaneado de biblioteca en progreso.
* S: Comienzo de pistas (programado).
* Shift+S: tiempo hasta el que se reproducirá la pista seleccionada
  (comienzos de pistas).
* T: modo editar/insertar Cart activado/desactivado.
* U: Studio al día.
* Control+Shift+U: busca actualizaciones del complemento.
* W: clima y temperatura si se configuró.
* Y: Estado modificado de lista de reproducción.
* 1 hasta 0 (6 para Studio 5.0x): anuncia el contenido de la columna para
  una columna específica.
* F8: toma instantáneas de la lista de reproducción (número de pistas, pista
  más larga, etc.).
* Shift+F8: Solicita transcripciones de la lista de reproducción en varios
  formatos.
* F9: Mark current track for start of playlist analysis (playlist viewer
  only).
* F10: realiza el análisis de tiempo de la pista (sólo visualizador de lista
  de reproducción).
* F12: cambia entre el perfil actual y uno predefinido.
* F1: Ayuda de la capa.
* Shift+F1: abre la guía del usuario en línea.

## SPL Controller

El SPL Controller es un conjunto de comandos de capas que puedes utilizar
para el control del SPL Studio desde cualquier lugar. Pulsa la orden de capa
del SPL Controller, y NVDA dirá, "SPL Controller." Pulsa otra orden para
controlar varias opciones del Studio tales como micrófono
activado/desactivado o reproducir la siguiente pista.

Las órdenes disponibles para el SPL Controller son:

* Pulsa P para reproducir la siguiente pista seleccionada.
* Pulsa U para pausar o no pausar la reproducción.
* Pulsa S para detener la pista con desvanecimiento, o para detener la pista
  instantáneamente, pulsa T.
* Pulsa M o Shift+M para activar o desactivar el micrófono, respectivamente,
  o pulsa N para habilitar el micrófono sin fade.
* Pulsa A para permitir la automatización oShift+A para desactivarla.
* Pulsa L para permitir la entrada de línea auxiliar o shift+L para
  desactivarla.
* Pulsa R para escuchar el tiempo restante para la pista actual en
  reproducción.
* Pulsa Shift+R para obtener un informe sobre el progreso del escaneado de
  la biblioteca.
* Pulsa C para permitir a NVDA anunciar el nombre y la duración de la pista
  actualmente en reproducción.
* Pulsa Shift+C para permitir a NVDA anunciar el nombre y la duración de la
  pista actualmente en reproducción si la hay.
* Pulsa E para obtener una cuenta y etiquetas de los codificadores que están
  siendo monitorizados.
* Pulsa I para obtener el recuento de oyentes.
* Pulsa Q para obtener información de estado variada acerca de Studio
  incluyendo si una pista se está reproduciendo, si el micrófono está
  encendido y otra.
* Pulsa las teclas de cart (F1, Control+1, por ejemplo) para reproducir
  carts asignados desde cualquier lugar.
* Pulsa H para mostrar un diálogo de ayuda que liste  las órdenes
  disponibles.

## Alarmas de pista

Por defecto, NVDA reproducirá un pitido si quedan cinco segundos a la
izquierda de la pista (outro) y/o intro. Para configurar este valor así como
para habilitarlos o deshabilitarlos, pulsa Alt+NVDA+1 o Alt+NVDA+2 para
abrir los diálogos fin de la pista y canción ramp, respectivamente. Además,
utiliza las opciones del diálogo del complemento Studio para configurar si
escucharás un pitido, un mensaje o ambos cuando se enciendan las alarmas.

## Alarma de micrófono

Puedes pedir a NVDA reproducir una canción cuando el micrófono haya sido
activado un rato. Pulsa Alt+NVDA+4 para configurar el tiempo de alarma en
segundos (0 la deshabilita).

## Track Finder

Si deseas encontrar rápidamente una canción por un artista o por el nombre
de la canción, desde la lista de pistas, pulsa Control+NVDA+F. Teclea el
nombre del artista o el nombre de la canción. NVDA te colocará en la canción
si la encontró o mostrará un error si no pudo encontrar la canción que estás
buscando. Para encontrar una canción o artista introducidos anteriormente,
pulsa NVDA+Shift+F3 para buscarla hacia adelante o atrás.

Nota: Track Finder es sensible a las mayúsculas.

## Explorador Cart

Dependiendo de la edición, SPL Studio permite hasta 96 carts para asignar
para la reproducción. NVDA te permite escuchar que cart, o jingle se asignó
a estas órdenes.

Para aprender las asignaciones de los cart, desde SPL Studio, pulsa
Alt+NVDA+3. Pulsando la  orden del cart una vez te dirá que  jingle se
asigna a  la orden. Pulsando la orden del cart dos veces reproducirá el
jingle. Pulsa Alt+NVDA+3 para salir del explorador de cart. Mira la guía del
complemento para más información sobre el explorador de carts

## Análisis de tiempo de la pista

Para obtener ancho para reproducir las pistas seleccionadas, marca la pista
actual para iniciar el análisis de tiempo de la pista (SPL Assistant, F9),
entonces pulsa SPL Assistant, F10 cuando se llegue a la selección final.

## Explorador de Columnas

Pulsando Control+NVDA+1 hasta 0 (6 para Studio 5.0x) o SPL Assistant, 1
hasta 0 (6 para Studio 5.01 y anteriores), puedes obtener contenidos de
columnas especificadas. Por omisión, hay artista, título, duración, intro,
categoría y Nombre de fichero (Studio 5.10 añade año, álbum, género y tiempo
programado). Puedes configurar qué columnas se explorarán a través del
diálogo Explorador de columnas que se encuentra en el diálogo de opciones
del complemento.

## Instantáneas de lista de reproducción

Puedes pulsar SPL Assistant, F8 mientras se enfoque sobre una lista de
reproducción en Studio para obtener varias estadísticas acerca de una lista
de reproducción, incluyendo el número de pistas en la lista, la pista más
larga, lista de artistas y así. Después de asignar una orden personalizada
para esta característica, pulsar dos veces la orden personalizada hará que
NVDA presente la información de la instantánea de la lista de reproducción
como una página web tal que puedas utilizar el modo exploración para navegar
(pulsa escape para cerrar).

## Playlist Transcripts

Pulsando en SPL Assistant, Shift+F8 presentará un cuadro de diálogo para
permitirte solicitar transcripciones de lista de reproducción en varios
formatos, incluyendo en un formato de texto plano, y tabla HTML o una lista.

## Diálogo de configuración

Desde la ventana de studio, puedes pulsar Alt+NVDA+0 para abrir el diálogo
de configuración del complemento. Alternativamente, ve al menú Preferencias
de NVDA y selecciona el elemento Opciones de SPL Studio. Este diálogo
también se utiliza para administrar los perfiles de transmisión.

## Modo táctil de SPL

Si estás utilizando Studio en un ordenador con pantalla táctil ejecutando
Windows 8 o posterior y tienes NVDA 2012.3 o posterior instalado, puedes
realizar algunas órdenes de Studio desde la pantalla táctil. Primero utiliza
un toque con tres dedos para cambiar a modo SPL, entonces utiliza las
órdenes táctiles listadas arriba para llevar a cabo tareas.

## Version 18.05

* Added ability to take partial playlist snapshots. This can be done by
  defining analysis range (SPL Assistant, F9 at the start of the analysis
  range) and moving to another item and performing playlist snapshots
  command.
* Added a new command in SPL Assistant to request playlist transcripts in a
  number of formats (Shift+F8). These include plain text, an HTML table, or
  an HTML list.
* Various playlist analysis features such as track time analysis and
  playlist snapshots are now grouped under the theme of "Playlist Analyzer".

## Versión 18.04.1

* NVDA ya no fallará al comenzar el temporizador de cuenta atrás para
  perfiles de retransmisión basados en tiempo si se está utilizando NVDA con
  el wxPython 4 toolkit instalado.

## Versión 18.04

* Se han realizado cambios para hacer la característica de verificar
  actualizaciones más fiable, especialmente si la verificación automática de
  actualizaciones del complemento está activada.
* NVDA reproducirá un tono para indicar el comienzo del escaneo de
  biblioteca cuando esté configurado para reproducir pitidos para anuncios
  diversos.
* NVDA comenzará a escanear la biblioteca en segundo plano si el escaneo se
  invoca desde el diálogo de opciones de Studio o automáticamente al
  arrancar.
* Tocar dos veces sobre una pista en la pantalla táctil o realizando el
  comando de acción por defecto seleccionará la pista y moverá el foco del
  sistema a ella.
* Se han resuelto varios errores cuando se toman capturas de listas de
  reproducción (asistente SPL, F8) que solo tienen marcadores horarios.

## Versión 18.03/15.14-LTS

* Si NVDA está configurado para anunciar el estado de emisión de metadatos
  cuando Studio se inicia, NVDA atenderá a esta configuración y ya no
  anunciará el estado de emisión al alternar desde y a perfiles de cambio
  instantáneo.
* Si se cambia desde o a un perfil de cambio instantáneo y NVDA está
  configurado para anunciar el estado de emisión de metadatos cuando esto
  ocurra, no se anunciará la información varias veces cuando se alternen
  perfiles rápidamente.
* NVDA recordará cambiar al perfil basado en horario (si se definió para un
  evento) aunque se reinicie NVDA varias veces durante la emisión.
* Si está activo un perfil basado en horario con la duración de perfil
  establecida, NVDA volverá al perfil original cuando el perfil acabe aunque
  se abra y se cierre el diálogo de configuración.
* Si está activo un perfil basado en horario (particularmente durante la
  transmisión), no será posible cambiar los disparadores del perfil de
  emisión mediante el diálogo de configuración del complemento.

## Versión 18.02/15.13-LTS

* 18.02: debido a los cambios internos realizados para soportar puntos de
  extensión y otras características, se requiere de NVDA 2017.4.
* La actualización adicional no será posible en algunos casos. Esto incluye
  ejecutar NVDA desde código fuente o con el modo seguro activado. La
  comprobación de modo seguro también es aplicable a 15.13-LTS.
* Si se producen errores durante la comprobación de las actualizaciones,
  éstos se registrarán y NVDA te aconsejará que leas el registro de NVDA
  para obtener más detalles.
* En las opciones del complemento, no se mostrarán varios ajustes de
  actualización en la sección de parámetros avanzados, como el intervalo de
  actualización, si no se admite la actualización de complementos.
* NVDA ya no parecerá congelarse o no hacer nada al cambiar a un perfil de
  cambio instantáneo o a un perfil basado en el tiempo y NVDA está
  configurado para anunciar el estado de la transmisión de metadatos.

## Versión 18.01/15.12-LTS

* Al utilizar la distribución de JAWS para SPL Assistant, la orden buscar
  actualizaciones (Control+Shift+U) ahora funciona correctamente.
* Al cambiar las opciones de alarma de micrófono a través del diálogo alarma
  (Alt+NVDA+4), cambios tales como habilitar alarma y cambios al intervalo
  de alarma de micrófono se aplican cuando se cierre el diálogo.

## Versión 17.12

* Se requiere Windows 7 Service Pack 1 o posterior.
* Se mejoraron varias características del complemento con puntos de
  extensión. Esto permite que las características alarma del micrófono y
  streaming de metadatos respondan a cambios en perfiles de
  retransmisión. Esto requiere NVDA 2017.4.
* Cuando se salga de Studio, varios diálogos del complemento tales como
  Opciones de complemento, diálogos de alarma y otros se cerrarán
  automáticamente. Esto requiere NVDA 2017.4.
* Añadida una orden a SPL Controller para informar del nombre de la pista
  actual en reproducción desde cualquier sitio (c).
* Ahora puedes pulsar las teclas de cart (F1, por ejemplo) después de
  introducir SPl Controller layer para reproducir carts asignados desde
  cualquier lugar.
* Debido a cambios introducidos en wxPython 4 GUI toolkit, el diálogo
  Eliminar etiqueta de stream ahora es un cuadro combinado en lugar de un
  campo de entrada numérica.

## Versión 17.11.2

Esta es la última versión que soporta Windows XP, Vista y 7 sin el Service
Pack 1. La siguiente versión estable para estas versiones de Windows serán
una versión 15.x LTS.

* Si se utilizan versiones de Windows anteriores a Windows 7 Service Pack 1,
  no puedes cambiarte a los canales de desarrollo

## Versión 17.11.1/15.11-LTS

* NVDA ya no reproducirá tonos de error o ya no parecerá no hacer nada al
  utilizar Control+Alt+teclas de flecha izquierda o derecha para navegar por
  columnas en Track Tool 5.20 con una pista cargada. Debido a este cambio,
  al utilizar Studio 5.20, se requiere de la compilación 48 o posterior.

## Versión 17.11/15.10-LTS

* Soporte inicial para StationPlaylist Studio 5.30.
* Si la alarma de micrófono y/o el temporizador de intervalos están
  activados y si se sale de Studio mientras el micrófono está encendido,
  NVDA ya no reproducirá los tonos de alarma de micrófono desde ningún
  sitio.
* Al eliminar los perfiles de retransmisión y ocurre otro perfil para ser un
  perfil de cambio instantáneo, la bandera de cambio instantáneo no se
  debería borrar del perfil de cambio.
* Si eliminando un perfil activo que no es un cambio instantáneo o un perfil
  basado en tiempo, NVDA pedirá confirmación una vez más antes de proceder.
* NVDA aplicará las configuraciones correctas para las opciones de alarma de
  micrófono cuando los perfiles de cambio a través del diálogo opciones del
  complemento.
* Ahora puedes pulsar SPL Controller, H para obtener ayuda para el SPL
  Controller layer.

## Versión 17.10

* Si se utilizan versiones de Windows anteriores a Windows 7 Service Pack 1,
  no puedes cambiarf al canal de actualizaciones Test Drive Fast. Una
  versión futura de este complemento moverá al usuario de versiones antiguas
  de Windows a un canal de soporte dedicado.
* Varias configuraciones generales tales como pitidos de anunciado de
  estado, notificación de inicio y de fin de la lista de reproducción y
  otras  ahora se colocan en el nuevo diálogo opciones generales del
  complemento (accesible desde un botón nuevo en las opciones del
  complemento).
* Ahora es posible hacer las opciones del complemento de sólo lectura,
  utilizar sólo el perfil normal, o no cargar opciones desde disco cuando
  Studio arranque. Estas se controlan por nuevos parámetros de órdenes de
  línea específicos para este complemento.
* Al ejecutar NVDA desde el diálogo Ejecutar (Windows+R), ahora puedes pasar
  unos parámetros adicionales de línea de órdenes para cambiar cómo funciona
  el complemento. Estos incluyen "--spl-configvolatile" (opciones de sólo
  lectura), "--spl-configinmemory" (No cargar opciones desde disco), y
  "--spl-normalprofileonly" (utilizar sólo el perfil normal).
* Si se sale de Studio (no de NVDA) mientras un perfil de cambio instantáneo
  está activo, NVDA ya no dará un anuncio engañoso al cambiar a un perfil de
  cambio instantáneo cuando se utilice Studio de nuevo.

## Versión 17.09.1

* Como resultado del anuncio de NV Access en que NVDA 2017.3 será la última
  versión que soporte versiones de Windows anteriores a windows 7 Service
  Pack 1, el complemento Studio presentará un mensaje recordatorio acerca de
  esto si se ejecutan versiones antiguas de Windows. El fin del soporte para
  versiones antiguas de Windows de este complemento se programó para abril
  de 2018.
* NVDA ya no muestra diálogos de inicio y/o anuncia la versión de Studio si
  se inició con la bandera mínimo ajustada a (nvda -rm). la única excepción
  es el diálogo recordatorio de versión antigua de Windows.

## Versión 17.09

* Si un usuario entra en el diálogo opciones avanzadas en opciones del
  complemento mientras el canal de actualizaciones y el intervalo se
  configuró a Unidad Rápida de Pruebas y/o cero días, NVDA ya no presentará
  el mensaje de aviso de canal y/o de intervalo al salir de este diálogo.
* Las órdenes de lista de reproducción restante y análisis de tiempo de
  pista ahora requerirán que se cargue una lista de reproducción, y de lo
  contrario se mostrará un mensaje de error más preciso.

## Versión 17.08.1

* NVDA ya no fallará causando que Studio reproduzca la primera pista cuando
  esté conectado un codificador.

## Versión 17.08

* Cambios para actualizar las etiquetas de canales: try build ahora es Test
  Drive Fast, development channel es Test Drive Slow. Las compilaciones
  verdaderas "try" se reservarán para las compilaciones reales try que
  requieran que los usuarios instalen manualmente una versión test.
* El intervalo de actualización ahora puede configurarse a 0 (cero)
  días. Esto permite al complemento buscar actualizaciones cuando NVDA y/o
  SPL Studio arranquen. Se requerirá de una confirmación para cambiar el
  intervalo de actualización a cero días.
* NVDA ya no fallará al buscar actualizaciones del complemento si el
  intervalo de actualización se configura a 25 días o más.
* En la configuración del complemento, se añadió una casilla de verificación
  para permitir a NVDA reproducir un sonido cuando un escuchante solicite
  entrar. Para utilizar esto completamente, la ventana de peticiones debe
  desplegarse cuando llegue la petición.
* Al pulsar dos veces la orden tiempo de transmisión (NVDA+Shift+F12) ahora
  causará que NVDA anuncie los minutos y segundos restantes en la hora
  actual.
* Ahora es posible utilizar Buscador de Pista (Control+NVDA+F) para buscar
  nombres de pistas que hayas buscado antes seleccionando un término de
  búsqueda desde un historial de términos.
* Al anunciar el título de la pista actual o siguiente a través del SPL
  Assistant, ahora es posible incluir información acerca de qué reproductor
  interno de Studio reproducirá la pista (ej.: player 1).
* Añadida una opción en la configuración del complemento en anuncios de
  estado para incluir información del reproductor al anunciar el título de
  la pista actual y siguiente .
* Corregido un problema en la cola temporal y otros diálogos donde NVDA no
  anunciaría los nuevos valores al manipular temporizadores.
* NVDA puede suprimir el anunciado de encabezados de columna tales como
  Artista y Categoría cuando se revisan pistas en el visualizador de listas
  de reproducción. Esta es una opción específica del perfil de transmisión.
* Añadida una casilla de verificación en el diálogo de opciones del
  complemento para suprimir el anunciado  de los encabezados de columna al
  revisar pistas en el visualizador de listas de reproducción.
* Añadida una orden a SPL Controller para informar del nombre y la duración
  de la pista actual en reproducción desde cualquier sitio (c).
* Al obtener información de estado a través de SPL Controller (Q) mientras
  se utiliza Studio 5.1x, la información tal como estado del micrófono, modo
  edición del cart y otra también se anunciará además de reproducción y
  automatización.

## Versión 17.06

* Ahora puedes realizar la orden Buscador de Pista (Control+NVDA+F) mientras
  se carga una lista de reproducción pero la primera pista no se enfoca.
* NVDA ya no reproducirá tonos de error o no hará nada al buscar una pista
  hacia adelante desde la última pista o hacia atrás desde la primera,
  respectivamente.
* Pulsar NVDA+Subrimir del teclado numérico (NVDA+Suprimir en la
  distribución portátil) ahora anunciará la posición de la pista seguida del
  número de elementos en una lista de reproducción.

## Versión 17.05.1

* NVDA ya no fallará al guardar cambios para opciones de alarma desde varios
  diálogos de alarma (por ejemplo, Alt+NVDA+1 para alarma de fin de pista).

## Versión 17.05/15.7-LTS

* El intervalo de actualización ahora puede configurarse a 180 días. Para
  instalaciones predeterminadas, el intervalo de actualización se buscará
  cada 30 días.
* Corregido un fallo donde NVDA podrá reproducir tonos de error si Studio
  sale mientras está activo un perfil basado en tiempo.

## Versión 17.04

* Añadido el soporte básico de depuración del complemento registrando
  información variada mientras el complemento está activo con NVDA
  configurado para registrar la depuración (se requiere de NVDA 2017.1 y
  superior). Para utilizar esto, antes de instalar NVDA 2017.1, desde el
  diálogo Salir de NVDA, elige la opción "reiniciar con el registro de
  depuración habilitado".
* Mejoras para la presentación de varios diálogos del complemento gracias a
  las características del NVDA 2016.4.
* NVDA descargará actualizaciones para el complemento en segundo plano si
  respondiste "sí" cuando se te preguntó para actualizar el
  complemento. Consecuentemente, ya no se te mostrarán las notificaciones de
  descarga del fichero desde los navegadores web.
* NVDA ya no parecerá colgarse al buscar una actualización al iniciarse
  debido a que cambie el canal de actualizaciones del complemento.
* Añadida la capacidad de pulsar Control+Alt+flecha arriba o abajo para
  moverse entre pistas (en especial, columnas de pista) verticalmente sólo
  según se mueve a la fila siguiente o anterior en una tabla.
* Añadida una casilla de verificación en el diálogo opciones del complemento
  para configurar qué columna debería anunciarse al moverse por las columnas
  verticalmente.
* Movidos los controles fin de pista, alarmas de intro y de micrófono desde
  las opciones del complemento al nuevo Centro de Alarmas.
* En el Centro de alarmas, los campos de edición de fin de pista e intro de
  pista siempre se muestran independientemente del estado de las casillas de
  verificación de notificación de alarma.
* Añadida una orden en el SPL Assistant para obtener instantáneas de listas
  de reproducción tales como número de pista, pista más larga, artistas
  principales y así (F8). también puedes añadir una orden personalizada para
  esta característica.
* Pulsando el gesto personalizado para instantáneas de lista de reproducción
  una vez permitirá a NVDA verbalizar y mostrar en braile una breve
  información instantánea. Pulsando la orden dos veces hará que NVDA abra
  una página web conteniendo una información más completa de la instantánea
  de la lista de reproducción. Pulsa escape para cerrar esta página web.
* Eliminado el Dial de Pista (versión mejorada de teclas de flechas de
  NVDA), reemplazado por las órdenes de navegación Explorador de Columnas y
  navegador de columnas/tablas ). Esto afecta a Studio y a Track Tool.
* Después de cerrar el diálogo Insertar Pistas mientras esté en progreso un
  escaneado de biblioteca, ya no se requiere pulsar SPL Assistant, Shift+R
  para monitorizar el progreso del escaneo.
* Mejorada la precisión de la detección y anunciado del completado de los
  escaneados de la biblioteca en Studio 5.10 y posterior. Esto corrige un
  problema donde el monitoreo de escaneado de la biblioteca finalizará
  prematuramente cuando hay más pistas a escanear, necesitando reiniciar el
  monitoreo de escaneado de la biblioteca.
* Mejorado el anunciado del estado del escaneo de biblioteca a través del
  SPL Controller (Shift+R) anunciando la cuenta de escaneo si el escaneado
  está ocurriendo.
* En la demo de Studio, cuando aparece la ventana de registro al iniciar
  Studio, las órdenes como tiempo restante para una pista ya no causará que
  NVDA no haga nada, reproduzca tonos de error, o dé información errónea. Se
  anunciará un mensaje de error en su lugar. Órdenes tales como estas
  requerirán que la ventana principal de Studio esté presente.
* Soporte inicial para StationPlaylist Creator.
* Añadida una nueva orden en SPL Controller layer para anunciar el estado de
  Studio como la reproducción de la pista y el estado del micrófono (Q).

## Versión 17.03

* NVDA ya no parecerá no hacer nada o no reproducirá un tono de error al
  cambiar a un perfil de transmisión basado en tiempo.
* Traducciones actualizadas.

## Versión 17.01/15.5-LTS

Nota: 17.01.1/15.5A-LTS reemplaza a 17.01 debido a cambios de la
localización de los ficheros nuevos del complemento.

* 17.01.1/15.5A-LTS: se cambió de dónde se descargan las actualizaciones
  para las versiones de soporte a largo plazo. Es obligatoria la instalación
  de esta versión.
* Mejorada la respuesta y la fiabilidad al utilizar el complemento para
  cambiar a Studio, o utilizando el foco para órdenes de Studio desde otros
  programas o cuando un codificador está conectado y se le pide a NVDA que
  cambie a Studio cuando esto ocurra. Si Studio se minimiza, la ventana de
  Studio se mostrará como no disponible. Si es así, restaura la ventana de
  Studio desde la bandeja del sistema.
* Si se editan carts mientras el explorador de Cart está activado, ya no es
  necesario reintroducir el explorador de Cart para ver las asignaciones de
  cart actualizadas cuando el modo Edición de Cart se
  desactive. Consecuentemente, el mensaje reintroducir explorador de Cart ya
  no se anuncia.
* En el complemento 15.5-LTS, se corrigió la presentación de la interfaz de
  usuario para el diálogo Opciones del complemento SPL.

## Versión 16.12.1

* Corregida la presentación de la interfaz de usuario para el diálogo
  Opciones del complemento SPL.
* Traducciones actualizadas.

## Versión 16.12/15.4-LTS

* Más trabajo sobre el soporte de Studio 5.20, incluyendo el anunciado del
  estado del modo inserción de cart (si está activado) desde el SPL
  Assistant layer (T).
* El conmutado del modo editar/insertar Cart ya no está afectado por la
  verbosidad de los mensajes ni por las opciones de anunciado del tipo de
  estado (Este estado se anunciará siempre a través de voz y/o braille).
* Ya no es posible añadir commentarios a las notas partidas.
* Soporte para Track Tool 5.20, incluyendo corregido un problema donde se
  anunciaba información errónea al utilizar las órdenes del Explorador de
  Columnas para anunciar información de columna.

## Versión 16.11/15.3-LTS

* Soporte inicial para StationPlaylist Studio 5.20, incluyendo la
  sensibilidad mejorada al obtener información de estado tal como estado de
  la automatización a través de SPL Assistant layer.
* Corregidos fallos relativos a la búsqueda de pistas e interactuación con
  ellas, incluyendo la incapacidad para marcar o desmarcar marcadores de
  pista o una pista encontrada a través del diálogo buscador de rango.
* El orden del anunciado de columnas ya no se revertirá al orden
  predeterminado después de cambiarlo.
* 16.11: Si los perfiles de transmisión tienen errores, el diálogo error ya
  no fallará al desplegarse.

## Versión 16.10.1/15.2-LTS

* Ahora puedes interactuar con la pista que se encontró a través del
  Buscador de Pistas (Control+NVDA+F) según la busques para reproducir.
* Traducciones actualizadas.

## Versión 8.0/16.10/15.0-LTS

La versión 8.0 (también conocida como 16.10) soporta SPL Studio 5.10 y
posteriores, con 15.0-LTS (antes 7.x) diseñada para proporcionar algunas
características nuevas de 8.0 para usuarios que utilicen versiones
anteriores de Studio. Al menos que se indique lo contrario, las entradas que
siguen se aplican tanto a 8.0 como a 7.x. Se mostrará un diálogo de
advertencia la primera vez que utilices el complemento 8.0 con Studio 5.0x
instalado, pidiéndote que utilices la versión 15.x LTS.

* El esquema de la versión ha cambiado para reflejar el año/mes de la
  publicación en lugar de mayor.menor. Durante el período de transición
  (hasta mediados de 2017), versión 8.0 es sinónimo de versión 16.10, con
  7.x LTS designándose como 15.0 debido a cambios incompatibles.
* El código fuente del complemento ahora se publica en GitHub (repositorio
  localizado en https://github.com/josephsl/stationPlaylist).
* Añadido un diálogo de bienvenida que se lanza cuando Studio arranca
  después de instalar el complemento. Se aha añadido una orden (Alt+NVDA+F1)
  para reabrir este diálogo una vez cerrado.
* Cambios para varias órdenes del complemento, incluyendo la eliminación de
  el comuntado del anuncio de estado (Control+NVDA+1), reasignada la alarma
  de fin de pista a Alt+NVDA+1, el conmutador de explorador de Cart ahora es
  Alt+NVDA+3, el diálogo de alarma de micrófono es Alt+NVDA+4 y el diálogo
  opciones del complemento/codificador es Alt+NVDA+0. Esto se hizo para
  permitir que Control+NVDA+fila de números se asigne al Explorador de
  Columnas.
* 8.0: relajada la restricción del Explorador de Columnas en lugar del 7.x
  así los números del 1 al 6 pueden configurarse para anunciar columnas en
  Studio 5.1x.
* 8.0: la orden conmutar Dial de pista y la opción correspondiente en las
  opciones del complemento han quedado en desuso y se eliminarán 9.0. Esta
  orden permanecerá disponible en el complemento 7.x.
* Añadido Control+Alt+Inicio/Fin para mover el navegador de Columna a la
  primera o última columna en el visualizador de la lista de reproducción.
* Ahora puedes añadir, ver, cambiar o eliminar comentarios de pista
  (notas). Pulsa Alt+NVDA+C desde una pista en el visualizador de lista de
  reproducción para escuchar los comentarios de pista si se definieron,
  pulsa dos veces para copiar el comentario al portapapeles o tres veces
  para abrir un diálogo para editar los comentarios.
* Añadida la capacidad de notificar si existe un comentario de pista, así
  como una opción en las opciones del complemento para controlar cómo
  debería hacerse.
* Añadido un ajuste en el diálogo opciones del complemento para permitir a
  NVDA notificarte si has alcanzado la parte superior o inferior del
  visualizador de lista de reproducción.
* Al reiniciar las opciones del complemento, ahora puedes especificar lo que
  se reinicia. Por defecto, las opciones del complemento se reiniciarán, con
  cuadros combinados para reiniciar el perfil de cambio instantáneo, perfil
  basado en tiempo, opciones del codificador y borrado de comentarios de
  pista añadidos al diálogo de opciones de reiniciado.
* En la Herramienta Pista, puedes obtener información sobre el álbum y
  código de CD pulsando Control+NVDA+9 y Control+NVDA+0, respectivamente.
* Se realizan mejoras al obtener información de columna por primera vez en
  la Herramienta de Pista.
* 8.0: añadido un diálogo en las opciones del complemento para configurar
  los slots del Explorador de Columnas para la Herramienta de Pista.
* Ahora puedes configurar el intervalo de alarma de micrófono desde el
  diálogo Alarma de micrófono (Alt+NVDA+4).

## Versión 7.5/16.09

* NVDA ya no desplegará el diálogo de progreso de la actualización si el
  canal de actualización del complemento se ha cambiado.
* NVDA respetará el canal seleccionado de actualización cuando descargue
  actualizaciones.
* Traducciones actualizadas.

## Versión 7.4/16.08

La versión 7.4 también se conoce como 16.08 seguido del año.mes número de
versión para versiones estables.

* Es posible seleccionar el canal de actualización del complemento desde
  opciones/opciones avanzadas del complemento, para que se elimine más tarde
  en 2017. Para 7.4, los canales disponibles son beta, stable y long-term.
* Añadida una opción en opciones/Opciones avanzadas del complemento para
  configurar el intervalo de búsqueda de las actualizaciones   entre 1 y 30
  días (el predeterminado es 7 o búsquedas semanales).
* La orden SPL Controller y la orden para enfocar a Studio no estarán
  disponibles desde pantallas seguras.
* Traducciones nuevas y actualizadas y añadida documentación localizada en
  varios idiomas.

## Cambios para 7.3

* Ligeras mejoras en el rendimiento al buscar información tal como
  automatización a través de algunas órdenes de SPL Assistant.
* Traducciones actualizadas.

## Cambios para 7.2

* Debido a la eliminación del antiguo estilo del formato de configuración
  interna, es obligatorio instalar el complemento 7.2. Una vez instalado, no
  puedes volver a una versión anterior del complemento.
* Añadida una orden en SPL Controller para informar del recuento de oyentes
  (I).
* Ahora puedes abrir los diálogos de opciones de SPL y opciones del
  codificador pulsando Alt+NVDA+0. Todavía puedes utilizar Control+NVDA+0
  para abrir estos diálogos (se eliminará en el complemento 8.0).
* En la Herramienta Pista, puedes utilizar Control+Alt+flechas izquierda o
  derecha para navegar entre columnas.
* Los contenidos de varios diálogos de Studio tales como el diálogo Acerca
  en Studio 5.1x ahora se anuncian.
* En los Codificadores SPL, NVDA silenciará el tono de conexión si
  auto-conectar está habilitado y entonces se apaga desde el menú de
  contexto del codificador mientras el codificador seleccionado se esté
  conectando.
* Traducciones actualizadas.

## Cambios para 7.1

* Corregidos erorres encontrados al actualizar desde el complemento 5.5 y
  anteriores al 7.0.
* Al responder "no" cuando se reinician las opciones del complemento, se
  volverá al diálogo de opciones del complemento y NVDA recordará la
  configuración del perfil cambio instantáneo.
* NVDA te preguntará para reconfigurar etiquetas de cadena y otras opciones
  del codificador si el fichero de configuración del codificador se
  corrompió.

## Cambios para 7.0

* Aññadida la característica buscar actualización del complemento. Esto
  puede hacerse manualmente (SPL Assistant, Control+Shift+U) o
  automáticamente (configurable a través del diálogo opciones avanzadas
  desde las opciones del complemento).
* Ya no se requiere estar  en la ventana visualizador de lista de
  reproducción para poder llamar a la mayoría de las órdenes de la capa SPL
  Assistant ­­­­­o obtener anunciados del tiempo tales como tiempo restante
  para la pista y el tiempo de retransmisión.
* Cambios para las órdenes del SPL Assistant, incluyendo duración de la
  lista de reproducción (D), reasignación de la selección de la duración en
  horas desde Shift+H a Shift+S y Shift+H ahora se utiliza para anunciar la
  duración de las pistas restantes para el actual slot horario, reasignada
  la orden estado de los metadatos del streaming (1 hasta 4, 0 es ahora
  Shift+1 hasta Shift+4, Shift+0).
* Ahora es posible invocar el buscador de pistas a través de SPL Assistant
  (F).
* SPL Assistant, números 1 hasta 0 (6 para Studio 5.01 y anteriores) pueden
  utilizarse para anunciar columnas de información específica. Estos slots
  de columnas pueden cambiarse con el elemento Explorador de Columnas en el
  diálogo Opciones del complemento.
* Corregidos numerosos errores informados por los usuarios al instalar el
  complemento 7.0 por primera vez cuando no se habían instalado estas
  versiones previas.
* Mejoras al Dial de pista, incluyendo mejorada la capacidad de respuesta al
  moverse a través de las columnas  y el seguimiento de columnas ahora se
  presenta en la pantalla.
* Añadida la habilidad para pulsar Control+Alt+flechas izquierda o derecha
  para moverse entre columnas de pista.
* Ahora es posible utilizar una distribución de órdenes diferente de lector
  de pantalla para las órdenes del SPL Assistant. Ve al diálogo Opciones
  avanzadas desde las opciones del complemento para configurar esta opción
  entre las distribuciones NVDA, JAWS y Window-Eyes. Consulta las órdenes
  del SPL Assistant más arriba para detalles.
* NVDA puede configurarse para cambiar a un perfil de retransmisión
  específico en un día específico y hora. Utiliza el nuevo diálogo
  Disparadores en las opciones del complemento para configurar esto.
* NVDA anunciará el nombre del perfil al que se cambie a través de cambio
  instantáneo (SPL Assistant, F12) o como un resultado del perfil basado en
  tiempo que está activándose.
* Movido el conmutador de cambio instantáneo (ahora una casilla de
  verificación) al nuevo diálogo disparadores.
* Las entradas en el cuadro combinado perfiles en el diálogo opciones del
  complemento ahora muestran banderas de perfil tales como activo, si es un
  perfil de cambio instantáneo y otros.
* Si se encuentra un problema serio con la lectura de los ficheros de
  perfiles de retransmisión, NVDA presentará un diálogo de error y
  reiniciará las opciones a las predeterminadas en lugar de no hacer nada o
  de hacer sonar un tono de error.
* Las opciones se guardarán en disco si y sólo si cambias opciones. Esto
  prolonga la vida de los SSDs (unidades de disco de estado sólido)
  previniendo guardados innecesarios en disco si las opciones no han
  cambiado.
* En el diálogo de opciones del complemento, los controles utilizados para
  conmutar el anunciado del tiempo programado, cuenta de oyentes, nombre de
  cart y nombre de pista se han movido a un diálogo dedicado al estado de
  los anunciados (selecciona el botón estado de los anunciados para abrir
  este diálogo).
* Añadido un ajuste nuevo en el diálogo opciones del complemento para
  permitir a NVDA reproducir pitidos para diferentes categorías de la pista
  al moverse entre pistas en el visualizador de lista de reproducción.
* Al intentar abrir la opción de configuración de metadatos en el diálogo
  opciones del complemento mientras el diálogo rápido de metadatos del
  streaming está abierto ya no causará que NVDA no haga nada o reproduzca un
  tono de error. NVDA ahora te pedirá cerrar el diálogo de metadatos del
  streaming antes de que puedas abrir las opciones del complemento.
* Cuando se anuncia tiempo tal como tiempon restante para la pista en
  reproducción, las horas también se anuncian. Consecuentemente, la opción
  anunciado de hora está habilitada por omisión.
* Pulsando SPL Controller, R ahora causa que NVDA anuncie el tiempo restante
  en horas, minutos y segundos (minutos y segundos si esto es tal caso).
* En los codificadores, al pulsar Control+NVDA+0 presentará el diálogo
  opciones del codificador para configurar varias opciones tales como
  etiqueta de cadena, enfocar a Studio al conectar y otras.
* En los codificadores, ahora es posible apagar los tonos de progreso de la
  conexión (configurable desde el diálogo opciones del codificador).

## Cambios para 6.4

* Se ha corregido un problema importante cuando se regresa desde un perfil
  de cambio instantáneo y el perfil de cambio instantáneo se activa de
  nuevo, visto después de eliminar un perfil que se colocó justo antes del
  perfil activo anteriormente. Al intentar eliminar un perfil, se mostrará
  un diálogo de aviso si está activo un perfil de cambio instantáneo.

## Cambios para 6.3

* Mejoras internas de seguridad.
* Cuando el complemento 6.3 o posterior se lanza primero en un ordenador
  ejecutando Windows 8 o posterior con NVDA 2016.1 o posterior instalado, se
  mostrará un diálogo de alerta preguntándote para desactivar el modo de
  atenuación de audio (NVDA+Shift+D). Selecciona la casilla de verificación
  para suprimir este diálogo en el futuro.
* Añadida una orden para enviar información de fallos, sugerencias de
  características y otra retroalimentación para el desarrollador del
  complemento (Control+NVDA+guión ("-")).
* Traducciones actualizadas.

## Cambios para 6.2

* Corregido un fallo con la orden resto de la lista de reproducción (SPL
  Assistant, D (R si el modo de compatibilidad está activado)) donde la
  duración para la hora actual fue anunciada como opuesta a la lista de
  reproducción entera (el comportamiento de esta orden se puede configurar
  desde las opciones avanzadas que se encuentra en el diálogo opciones del
  complemento).
* NVDA ahora puede anunciar el nombre de la pista en reproducción actual
  mientras se utiliza otro programa (configurable desde las opciones del
  complemento).
* Ahora se hace caso a La opción utilizada para permitir a la orden SPL
  Controller invocar a SPL Assistant (panteriormente se habilitaba en todas
  las ocasiones).
* En los codificadores SAM, las órdenes Control+F9 y Control+F10 ahora
  funcionan correctamente.
* En los codificadores, cuando un codificador se enfoca primero y si este
  codificador se configura para ser monitorizado en segundo plano, NVDA
  ahora iniciará el monitorizado en segundo plano automáticamente.

## Cambios para 6.1

* Anunciado de orden de columna e inclusión, así como de las opciones de los
  metadatos del streaming ahora opciones del perfil específico.
* Al cambiar los perfiles, se habilitarán las cadenas correctas de
  metadatos.
* Al abrir el diálogo de opciones rápidas de metadatos del streaming (orden
  no asignada), las opciones cambiadas ahora se aplican al perfil activo.
* Al iniciar Studio, se cambió cómo se muestran los errores si sólo el
  perfil corrupto es el perfil normal.
* Al cambiar ciertas opciones utilizando atajos de teclado tales como el
  anunciado de estado, se corrigió un problema donde la opción cambiada no
  se mantenía cuando se cambiaba y desde un perfil de cambio instantáneo.
* Al utilizar una orden de SPL Assistant con un gesto personalizado definido
  (tal como la orden pista siguiente), ya no requiere estar en el
  visualizador de lista de reproducción de Studio para utilizar estas
  órdenes (pueden realizarse desde otras ventanas de Studio).

## Cambios para 6.0

* Nuevas órdenes de SPL Assistant, incluyendo el anunciado de título de la
  pista actualmente en reproducción (C), el anunciado del estado de
  metadatos del streaming (E, 1 hasta 4 y 0) y la apertura de la guía del
  usuario en línea (Shift+F1).
* Capacidad para empaquetar opciones favoritas como perfiles de emisión para
  utilizarse durante un show y para cambiar a un perfil
  predefinido. Consulta la guía del complemento para detalles sobre perfiles
  de emisión.
* Añadida una nueva opción en opciones del complemento para controlar la
  verbosidad de los mensajes (algunos mensajes se acortarán cuando la
  verbosidad avanzada esté seleccionada).
* Añadida una nueva opción en opciones del complemento para permitir a NVDA
  anunciar horas, minutos y segundos para las órdenes duración de la pista o
  lista de reproducción (las características afectadas incluyen el anunciado
  de tiempo transcurrido y restante para la pista actualmente en
  reproducción, al análisis de tiempo de pista y otros).
* Ahora puedes pedir a NVDA que informe de la longitud total de un rango de
  pistas a través de la característica de análisis de tiempo de la
  pista. Pulsa SPL Assistant, F9 para marcar la pista actual como marcador
  de comienzo, muévete al final del rango de pista y pulsa SPL Assistant,
  F10. Estas órdenes pueden reasignarse así una no tenga que invocar a SPL
  Assistant layer para realizar el análisis de tiempo de la pista.
* Añadido un diálogo buscar columna (orden no asignada) para encontrar texto
  en columnas específicas tales como artista o parte de nombre de fichero.
* Añadido un diálogo buscador de rango de tiempo (orden no asignada) para
  encontrar una pista con duración que caiga dentro de un rango
  especificado, útil si se desea encontrar una pista para rellenar una hora.
* Añadida la capacidad de reordenar el anunciado de las columnas de la pista
  y para suprimir el anunciado de columnas específicas si "utilizar orden de
  pantalla" está desmarcado desde el diálogo de opciones del
  complemento. Utiliza el diálogo "administrar anunciado de columna" para
  reordenar columnas.
* Añadido un diálogo (orden no asignada) para conmutar cíclicamente
  metadatos del streaming.
* Añadida una opción en el diálogo opciones del complemento para configurar
  cuando el estado de los metadatos del streaming debería anunciarse y para
  habilitar metadatos del streaming.
* Añadida la capacidad para marcar una pista como un marcador para volver a
  él más tarde (SPL Assistant, Control+K para ponerlo, SPL Assistant, K para
  moverse a la pista marcada).
* Mejora del rendimiento al buscar siguiente o anterior texto de pista
  conteniendo el texto buscado.
* Añadida una opción en el diálogo opciones del complemento para configurar
  notificación de alarma (pitido, mensaje o ambos).
* Ahora es posible configurar la alarma del micrófono entre 0
  (deshabilitado) y dos horas (7200 segundos.) y utiliza flecha arriba y
  flecha abajo para configurar esta opción
* Añadida una opción en el diálogo de opciones del complemento para permitir
  al micrófono activar una notificación para una periodicidad dada.
* Ahora puedes usar la orden conmutar Dial de pista en Studio para conmutar
  el dial de pista en Herramienta de Pista ya que no se asignaba una orden
  para conmutar Dial de Pista en la Herramienta de Pista.
* Añadida la capacidad para utilizar la orden de capa de SPL Controller para
  invocar SPL Assistant (configurable desde el diálogo Opciones avanzadas
  que se encuentra en el diálogo de opciones del complemento).
* Añadida la capacidad para que NVDA utilice ciertas órdenes de SPL
  Assistant utilizadas por otros lectores de pantalla. Para configurar esto,
  ve a opciones del complemento, selecciona Opciones Avanzadas y marca la
  casilla de verificación modo de compatibilidad de lectores de pantalla.
* En los codificadores, opciones tales como el enfocado de Studio cuando se
  esté conectado ahora se recuerdan.
* Ahora es posible ver varias columnas desde la ventana del codificador
  (tales como estado de conexión del codificador) a través de la orden
  Control+NVDA+número; consulta las órdenes del codificador arriba.
* Corregido un extraño fallo donde al cambiar a Studio o al cerrar un
  diálogo de NVDA (incluyendo el diálogo del complemento Studio) impedía que
  órdenes de pista (tales como el conmutado de Dial de pista) funcionasen
  como se esperaba.

## Cambios para 5.6

* En Studio 5.10 y posterior, NVDA ya no anuncia "no seleccionado" cuando la
  pista seleccionada se está reproduciendo.
* Debido a un problema con el mismo Studio, NVDA ahora anuncia el nombre de
  la pista actualmente en reproducción automáticamente. Se ha añadido una
  opción para conmutar este comportamiento en el diálogo de opciones del
  complemento studio.

## Cambios para 5.5

* La opción reproducir después de conectar se recordará al moverse a través
  de la ventana del codificador.

## Cambios para 5.4

* Al realizar un escaneado de la biblioteca desde el diálogo Insertar Pistas
  ya no se causa que NVDA no anuncie el estado del escaneado o reproduzca
  tonos de error si NVDA se configura para anunciar el progreso del
  escaneado de biblioteca o cuenta de escaneado.
* Traducciones actualizadas.

## Cambios para 5.3

* Ahora está disponible la corrección para el Codificador SAM (no reproduce
  la siguiente pista si una pista está en reproducción y cuando el
  codificador se conecta) para los usuarios del codificador SPL.
* NVDA ya no reproduce errores o no hace nada cuando SPL Assistant, F1
  (Diálogo de ayuda de Assistant) esté pulsado.

## Cambios para 5.2

* NVDA ya no permitirá que se abran ambos diálogos de opciones y alarma. Se
  mostrará una advertencia pidiendo cerrar el diálogo anteriormente abierto
  antes de abrir otro diálogo.
* Cuando se monitorice uno o más codificadores, pulsando el SPL Controller,
  ahora se anunciará la cuenta de codificador, el identificador de
  codificador y la cadena de etiqueta(s) si la hubiese.
* NVDA soporta todas las órdenes connectar/desconectar
  (Control+F9/Control+F10) en codificadores SAM.
* NVDA ya no reproducirá la siguiente pista si un codificador se conecta
  mientras Studio esté reproduciendo una pista y se diga a Studio que
  reprodujese pistas cuando un odificador esté conectado.
* Traducciones actualizadas.

## Cambios para 5.1

* Ahora es posible revisar columnas individuales en Herramienta de Pista a
  través de Dial de pista (tecla conmutadora no asignada). Ten en cuenta que
  Studio debe estar activo antes de utilizar este modo.
* Añadida una casilla de verificación en el diálogo de opciones del
  complemento Studio para conmutar el anunciado del nombre del cart
  actualmente en reproducción.
* Al activar y desactivar el micrófono a través del SPL Controller ya no
  causa que se reproduzcan tonos de error o que cambie el sonido a no ser
  reproducido.
* Si se asigna una orden personalizada a una orden de capa del SPL Assistant
  y esta orden se pulsa directamente después de entrar en SPL Assistant,
  NVDA ahora saldrá rápidamente del SPL Assistant.

## Cambios para 5.0

* Se ha añadido un diálogo de opciones dedicado para el complemento SPL,
  accesible desde el menú Preferencias de NVDA o pulsando Control+NVDA+0
  desde la ventana del SPL.
* Añadida la capacidad para reiniciar todas las opciones a las
  predeterminadas a través del diálogo de configuración.
* Si algunas de las opciones tienen errores, sólo se reiniciarán las
  opciones afectadas a las predeterminadas de fábrica.
* Añadido un modo SPL de pantalla táctil dedicado y órdenes táctiles para
  realizar varias funciones de Studio.
* Cambios a SPL Assistant layer incluyen la adición de la orden de capa de
  ayuda (F1) y la eliminación de las órdenes para conmutar la cuenta de
  oyentes (Shift+I) y anunciado de tiempo programado (Shift+S). puedes
  configurar estas opciones en el diálogo de opciones del complemento.
* Renombrado "conmutar anunciado" para "anunciado de estado" ya que los
  pitidos se utilizan para el anunciado de otra información de estado tal
  como el completado de los escaneos de la biblioteca.
* La opción de anunciado de estado ahora se mantiene a través de las
  sesiones. Anteriormente tenías que configurar esta opción manualmente
  cuando Studio arrancaba.
* Ahora puedes utilizar la característica Dial de Pista para revisar
  columnas en una pista de entrada en el visualizador de la lista de
  reproducción principal de Studio (para conmutar esta característica, pulsa
  la orden que asignaste para esta característica).
* Ahora puedes asignar órdenes personalizadas para escuchar la información
  de temperatura o para anunciar el título para la pista siguiente si se
  programó.
* Añadida una casilla de verificación en los diálogos final de la pista y
  alarma de intro de la canción para activar o desactivar estas alarmas
  (marca para activar). estos también pueden "configurarse" desde las
  opciones del complemento.
* Corregido un fallo al pulsar órdenes de diálogo de alarma o buscador de
  pistas mientras otro diuálogo de alarma o buscador esté abierto que
  causaría que otra instancia del mismo diálogo aparezca. NVDA abrirá un
  mensaje preguntándote para cerrar el diálogo previamente abierto primero.
* Cambios y correcciones para el explorador de Cart, incluyendo la
  exploración errónea de bancos de cart cuando el usuario no esté enfocando
  el visualizador de la lista de reproducción. El explorador de Cart ahora
  verificará para estar seguro de que estás en el visualizador de lista de
  reproducción.
* Añadida la capacidad para utilizar la orden de capa de SPL Controller para
  invocar SPL Assistant (experimental; consulta la guía del complemento
  sobre cómo habilitar esto).
* En el codificador windows, la orden de anunciado de hora y fecha NVDA
  (NVDA+F12 por omisión) anunciará la hora incluyendo segundos.
* Ahora puedes monitorizar codificadores individuales para estado de
  conexión y para otros mensajes pulsando Control+F11 mientras que el
  codificador que deseas monitorizar esté enfocado (funciona mejor cuando se
  utiliza codificadores SAM).
* Añadida una orden en SPL Controller layer para anunciar el estado de los
  codificadores que estén siendo monitorizados (E).
* Ya está disponible una solución para arreglar un problema donde NVDA
  anunciaba etiquetas de cadena para los codificadores equivocados, sobre
  todo después de la eliminación de un codificador )para realinear etiquetas
  de cadena, pulsa Control+F12, después selecciona la posición del
  codificador que has eliminado).

## Versiones antiguas

Por favor consulta el enlace changelog para notas de la versión para
versiones antiguas del complemento.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: http://josephsl.net/files/nvdaaddons/get.php?file=spl-lts16

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide
