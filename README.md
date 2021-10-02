# OVERIDE - Proyecto app gestion viajes

## Acerca de la app


Overide es una applicacion creada con el fin de poder gestionar la compra de pasajes de buses intermunicipales.
Esta aplicacion esta creada como proyecto para el ciclo 3 de MisionTic20222

## Tecnologias utilizadas

La applicacion fue contruida usando las siguientes tecnologias:

* PostgreSQL
* Django
* React

## Instalacion y configuracion

Una vez clonado el repositorio y creado el entorno virtual, se debe ingresar a la carpeta requirements y con el entorno virtual activado se debe ejecutar el comando

```console
pip install -r local.txt
```

El proyecto de desarrollo esta corriendo con SQLite3 como base de datos por lo tanto no es necesario realizar configuraciones adicionales.

Una vez se han realizado las configuraciones se debe ejecutar el comando en la misma carpeta que contiene el manage.py con el fin de realizar las migraciones a la base de datos

```console
python manage.py makemigrations
```

Una vez se han configurado las migraciones se deben implementar con el comando

```console
python manage.py migrate
```

Finalmente se puede ejecutar el servidor de desarrollo con el comando

```console
python manage.py runserver
```

## Notas

0.1.0  

* Cambios al diseño base del proyecto
* Agregada configuracion de postgres (controlador y conexion local en el archivo base.py)
* Agregados modelos de las apps personas, viajes, pasajeros, buses, trayectos y ciudades.
* Agregados modelos al administrador de Django

0.1.1

* Cambios en las apps del proyecto
* Agregadas configuraciones de visualizacion en el administrador
* Agregadas caracteristica de autoasignacion de valor de los campos codigo de acuerdo a la tabla y a sus valores principales

0.2.0

* Cambios a las apps del proyecto
* Agregadas nuevas configuraciones de visualizacion en el administrador
* Eliminadas apps exepto Usuarios el cual pasa a llamarse Users
* Agregada opcion de creacion de usuarios y superusuarios en el administrador
* Agregada opcion para subir imagen y asociarla a un usuario
* Agregados servicios REST para la aplicacion Users (ver users/api)
