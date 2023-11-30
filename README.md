# TrafficWatch

Aplicación de alerta de autos sospechosos reconocido por medio de camaras de vigilancia y inteligencia artificial

## Clonación del Repositorio

### Usando HTTP

```bash
git clone https://github.com/Nispeter/PI_2023-2.git
```

### Usando SSH

```bash
git clone git@github.com:Nispeter/PI_2023-2.git
```
## Frontend

### Requisitos Previos

- Node.js: Debes tener Node.js instalado en tu sistema. Puedes descargarlo desde la página [oficial de Node.js](https://nodejs.org/).

### Instalación de pnpm

pnpm es el administrador de paquetes utilizado para el frontend. Sigue estas instrucciones para instalarlo:

#### Windows

1. Abre PowerShell como administrador.
1. Ejecuta: `iwr https://get.pnpm.io/v6.16.js -useb | node`.

#### Linux

1. Abre la terminal.
1. Ejecuta: `curl -fsSL https://get.pnpm.io/v6.16.js | node - add --global pnpm`.

#### macOS

1. Abre la terminal.
1. Ejecuta: `curl -fsSL https://get.pnpm.io/v6.16.js | node - add --global pnpm`.

### Configuración de Archivo .env

1. En la carpeta del frontend, crea un archivo .env basándote en .env.example.
1. Copia el contenido de .env.example en .env.
1. Modifica los valores en .env según sea necesario.

### Ejecución del Proyecto

1. Navega a la carpeta del frontend.
1. Instala las dependencias con pnpm install.
1. Inicia el proyecto con `pnpm dev`.
1. Accede a la aplicación en http://localhost:5173.

## Backend

### Modelo
Obtendido de https://github.com/computervisioneng/automatic-number-plate-recognition-python-yolov8

### Ambiente 
- Crear un ambiente con python=3.8:\
```conda create --prefix ./env python==3.8 -y```
- Instalar las dependencias en el ambiente: \
```pip install -r requirements.txt```

### Uso chat bot
### Crear un Bot en Telegram y Obtener el `chat_id`

#### 1. Crear el Bot en Telegram
- Abre **Telegram** y busca el bot oficial llamado `BotFather`.
- Inicia una conversación con `BotFather` y utiliza el comando `/newbot`.
- Sigue las instrucciones para nombrar tu bot y asignarle un nombre de usuario. Debe terminar en `bot` (e.g., `mi_primer_bot`).
- `BotFather` te proporcionará un **token de acceso**. Guárdalo, es necesario para interactuar con la API de Telegram.

#### 2. Enviar un Mensaje al Bot
- Busca tu bot en Telegram usando el nombre de usuario creado.
- Inicia una conversación enviando cualquier mensaje.

#### 3. Obtener el `chat_id`
- Realiza una solicitud **HTTP GET** a la siguiente URL: `https://api.telegram.org/bot[TU_TOKEN]/getUpdates`
- Reemplaza `[TU_TOKEN]` con el token proporcionado por `BotFather`.
- La solicitud puede hacerse desde un navegador o herramientas como Postman.
- En la respuesta, localiza el campo `chat` bajo `message`, ahí encontrarás el `chat_id`.

**Nota:** El `chat_id` es único para cada conversación. 

#### 4. Poner el token y el chat_id en sus respectivas variables en lineas XX y XX. 
Desde backend/models/Automatic-License-Plate-Recognition-using-YOLOv8/
- En el script network_utils.py modificar la funcion sendTelegram() para que se utilice el bot con el chat deseado
### video
Debe tenerse el video sample.mp4 que será utilizado como si fuese una cámara dentro de la carpeta: 
backend/models/Automatic-License-Plate-Recognition-using-YOLOv8/
El video utilizado para testear es:
https://drive.google.com/file/d/1JbwLyqpFCXmftaJY1oap8Sa6KfjoWJta/view?usp=sharing 

### ejecucion

Dentro del ambiente desde backend/models/Automatic-License-Plate-Recognition-using-YOLOv8/
- Correr el Servidor:\
```python main.py```
- Correr el Cliente:\
```python client.py```
## Base de datos
### Instalacion
Desde backend/database/
- Crear ambiente\
```python -m venv venv```
- Activar el ambiente\
```./env/Scripts/activate```
- Alternativamente\
```source ./venv/bin/activate```
- Instalar las dependencias en el ambiente\
```pip install -r requirements.txt```
### Uso
Desde backend/database/
```uvicorn app:app```
Inferfaz de fast api para probar endpoints:\
127.0.0.1:8000/docs/\