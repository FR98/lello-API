<h2 align="center">Lello</h2>
<h3 align="center">Proyecto UVG WEB</h3>

## Configuración de entorno

* [Instalar Python](https://www.python.org/)
* [Instalar Postgres](https://www.postgresql.org/)
* Instalar Python Enviorment
    ```shell
    $ sudo apt install python3-env
    ```
* Clonar repo
* Crear y activar python env
    ```shell
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
* Instalar dependencias
    * Si es necesario, borrar de requirements pkg-resources==0.0.0 y psycopg2 ya que hay conflictos entre SO
    ```shell
    $ pip install -r requirements.txt
    ```
* [psycopg2](https://www.psycopg.org/)
    * Comprobar instalación
    ```shell
    $ python -c "import psycopg2" --verbose
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
