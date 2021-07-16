# Utilidades personalizadas para Sublime-Text 


## Funcionalidades disponibles:

+ **Pegar Texto-HTML**: Pega el contenido copiado de una página web en modo html, siendo el modo normal de pegado el de texto plano.
+ **Normalizar**: Reduce el texto seleccionado a los caracteres "a-z", "0-9", "_" y ".".
+ **Bash**: Ejecuta un bloque de texto como Bash, y agrega el resultado si lo hubiese.
+ **Python3**: Ejecuta un bloque de texto como Python3, y agrega el resultado si lo hubiese.
+ **Buscar en DDG**: Abre el navegador web por defecto y busca el texto seleccionado en el buscador DuckDuckGo.
+ **Calcular**: Calcula matemáticamente el texto seleccionado, devolviendo el resultado, si es válido. 
+ **Calcular Fracción**: Calcula matemáticamente el texto seleccionado, devolviendo el resultado en fracciones, si es válido.
+ **Calcular Decimal**: Calcula matemáticamente el texto seleccionado, devolviendo el resultado en decimales, si es válido.
+ **Youtube Título**: Devuelve el título de una url seleccionada de youtube (u otra web de las disponibles en youtube-dl).
+ **Texto desde URL**: Devuelve en modo texto plano todo el contenido de la url seleccionada.
+ **Fecha**: Devuelve la fecha al momento actual en formato AAAA-MM-DD hh:mm:ss:ms.
+ **Instante**: Devuelve el timestamp del momento actual.
+ **Instante a Fecha**: Devuelve la fecha de un timestamp seleccionado.
+ **Instante a Hora**: Devuelve la hora de un timestamp seleccionado.
+ **Duración**: Devuelve la diferencia de dos timestamps consecutivos seleccionados.
+ **Sumar Tiempos**: Devuelve la suma de varios tiempos seleccioandos.
+ **Terminal en carpeta actual**: Abrir una ventada de terminal en la ruta del documento actual.
+ **Abrir Recurso**: Si el path o la url son válidos la abre con el software por defecto del sistema operativo. El path puede ser obsoluto o relativo. La url debe comenzar con 'http'.

## Modo de uso

Copiar la carpeta "./utiles-sublime-package/":

+ en Linux, a: "~/.config/sublime-text-3/Packages/"
+ en Windows, a:  "%AppData%\Roaming\Sublime Text 3\Packages"


## Requerimientos de algunas utilidades

./utiles-sublime-package/extras/calcular_decimal.py

	decimal

./utiles-sublime-package/extras/calcular_fraccion.py

	fractions

./utiles-sublime-package/extras/extraer_texto_de_url.py

	pyquery

./utiles-sublime-package/extras/yt_info.py

	youtube_dl

./utiles-sublime-package/extras/clipboard_text_html.py

	GTK 3 (sólo para Linux)


