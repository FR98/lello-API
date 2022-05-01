<h1 align="center">Lello</h1>
<h2 align="center">Proyecto UVG WEB</h2>
<h3 align="center">Gian Luca Rivera - 18049</h3>
<h3 align="center">Francisco Rosal - 18676</h3>

## Configuración de entorno

* [Instalar Python](https://www.python.org/)
* [Instalar Postgres](https://www.postgresql.org/)
* Instalar Python Enviorment
    ```shell
    Linux:
    $ sudo apt install python3-env
    MacOS:
    $ sudo pip3 install virtualenv
    ```
* Clonar repo
* Crear y activar python env
    ```shell
    Linux:
    $ python3 -m venv venv
    $ source venv/bin/activate
    MacOS:
    $ virtualenv venv
    $ source venv/bin/activate
    ```
* Instalar dependencias
    * Si es necesario, borrar de requirements pkg-resources==0.0.0 y psycopg2 ya que hay conflictos entre SO
    ```shell
    $ pip install -r requirements.txt
    ```
* [psycopg2](https://www.psycopg.org/)
    * Instalar y comprobar instalación
    ```shell
    Linux:
    $ pip install psycopg2
    $ python -c "import psycopg2" --verbose
    MacOS:
    $ pip3 install psycopg2-binary
    $ python3 -c "import psycopg2" --verbose
    ```

## Configuración de Base de Datos

* Crear archivo /lello/credentials.py
    ```python
        DEVELOPMENT_DATABASE = {
            'NAME': 'lello_dev_db',
            'USER': 'tu-user',
            'PASSWORD': 'tu-password',
            'HOST': 'localhost',
            'PORT': '5432',
            'CONNECTION': 'postgres',
        }
    ```

* Crear/resetear la db y aplicar migrations
    ```shell
    $ cd lello
    $ python load_data.py
    ```

* Run Server
    ```shell
    $ python manage.py runserver
    ```

## Para ejecucion

* Clonar repo
* Configurar entorno (instalar dependencias de requirements.txt)
    * Borrar pkg-resources==0.0.0 y psycopg2 del requirements.txt si es necesario e instalarlo manualmente (Cambia por SO)
* Configuracion de DB y credenciales
* python load_data.py
    * Sirve para crear o resetear la db si se necesita y migraciones de Django
    * Para su uso correcto seleccionar la opcion 1 del menu y luego la 3
* python manage.py runserver
* Para cargar la db inicial ir a ruta: /admin/initial-data/
    * Usuarios ya registrados:
        Username: admin
        Password: admin
* Listo!

<h3 align="center">IMPORTANTE</h3>
 Para comprobar el funcionamiento de enviar emails, registrarse con un correo real y revisar la bandeja de entrada.
 
