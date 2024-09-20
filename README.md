# ImplementacionPylintBlack

## Descripcion del Proyecto

Este proyecto implementa un sistema CRUD para gestionar dos entidades: **Avión** y **Libro de Cocina**. La aplicación está desplegada y ejecutada utilizando contenedores Docker, lo que facilita su instalación y despliegue en cualquier entorno.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (para Windows o macOS)
- [Python 3.8+](https://www.python.org/downloads/)
- PyLint y Black (que se instalan automáticamente con `requirements.txt`)

## Cómo ejecutar el Proyecto

### 1. Clonar el Repositorio

Primero clona el repositorio en tu máquina local:
```bash
git clone https://github.com/blandoncj/ImplementacionPylintBlack.git
cd ImplementacionPylintBlack
```

### 2. Iniciar Docker Desktop

Si estás en Windows o macOS, asegúrate de que **Docker Desktop** esté instalado y corriendo.

### 3. Levantar la Aplicación con Docker

Una vez que Docker Desktop esté corriendo, ejecuta el siguiente comando desde el directorio del proyecto para levantar la aplicación

```bash
docker compose up -d
```
Esto levantará ambos contenedores, el del backend y el del adminer  

### 4. Verificar que los contenedores estén corriendo

Para asegurarte de que los contenedores están corriendo correctamente, usa el siguiente comando:

```bash
docker ps
```

### 5. Acceder a la API

El backend de la aplicación estará disponible en http://localhost:8000. Visita esta URL para interactuar con las APIs CRUD de las entidades **Avión** y **Libro de Cocina**

### 6. Acceder a Adminer (Gestión de Base de Datos)

Si deseas gestionar visualmente  la base de datos, puedes acceder a Adminer en la url http://localhost:8080. Adminer es una herramienta que te permite gestionar las tablas y registros de la base de datos en una interfaz web

## Uso de Pylint

Para verificar la calidad del código con Pylint, usa:

```bash
pylint <nombre_del_directorio>/
```

## Uso de Black

Para asegurarte de que el código cumple con PEP8, usa Black para formatearlo automáticamente:

```bash
black .
```

## Creadores

- **[Jacobo Blandón Castro](https://github.com/blandoncj)**
- **[Johan Antonio Peña López](https://github.com/Johan0425)**
