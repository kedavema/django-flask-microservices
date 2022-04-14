# Microservicios con Python, Docker y RabbitMQ

### Descripción

Proyecto de dos microservicios comunicados a través de eventos de RabbitMQ.

Consta de dos microservicios, uno con Django, y el otro con Flask, ambas con sus bases de datos en MySQL en contenedores Docker.

Se utilizó eventos de RabbitMQ para la comunicación entre ambos.

### Construcción 🛠️
* **Lenguaje:** Python 3
* **Contenedores** Docker
* **Eventos** RabbitMQ
* **Framework:** Django, Flask, SQL Alchemy

## Requisitos
- Docker instalado.
- Crear una cuenta en CloudAMQP y posteriormente crear una instancia para obtener el parámetro **AMQP URL**

## Instalación y ejecución:

- Clone o descargue el proyecto.
- Busque en el proyecto **URLParameters** y reemplácelo por el parametro obtenido de su cuenta de RabbitMQ(AMQP URL)

Ejecute cada comando ```docker-compose``` en diferentes terminales en sus respectivas carpetas de **admin** y **main**.

* Construir los contenedores: ```docker-compose build```

* Inicializar los microservicios: ```docker-compose up```

* Detener los servicios: ```docker-compose stop```

De forma predeterminada, los microservicios se ejecutarán en los siguientes puertos:
- admin: 8000
- main: 8001

#### Nota:
Las aplicaciones probablemente lanzarán una excepción la primera vez, porque intentarán conectarse al servicio MySQL que aún se está inicializando por primera vez; en este caso, espere a que MySQL se inicialice por completo primero y luego ejecute los comandos: 
`docker-compose restart adminbackend` y `docker-compose restart mainbackend` en otra terminal para reiniciar los servicios bloqueados.

### Antes de probar los endpoints
Con un gestor de bases de datos de su elección(por ejemplo DBeaver) cree instancias de usuarios, en la base de datos de Django.

### Probar la aplicación:
Para probar los endpoints basta con entrar al archivo req.http dentro de cada carpeta de los servicios, para ello debe tener instalado en su editor de código un cliente REST(por ejemplo **REST Client**, para Visual Studio Code).

### Endpoints creados:
- CRUD de productos en Django, al crearse productos en Django a travéz de un evento de RabbitMQ se crea automáticamente el mismo producto con el mismo ID en la base de datos de Flask
- Endpoint para likes de los productos, al darle like desde el endpoint de Flask automáticamente se aumenta el valor del mismo en la base de datos de Django.
