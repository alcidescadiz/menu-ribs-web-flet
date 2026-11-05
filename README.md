### Crear y activar entorno virtual

* python -m venv venv
* venv\Scripts\activate

### Ejecutar app

* flet run main.py
* flet publish   
* python -m http.server --directory build\web

### Complilar app

* flet build web
* flet build apk
* flet build windows