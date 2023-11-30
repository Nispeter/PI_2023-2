# Modelo
obtendido de https://github.com/computervisioneng/automatic-number-plate-recognition-python-yolov8
## Instalacion 
- Crear un ambiente con python=3.8:\
```conda create --prefix ./env python==3.8 -y```
- Instalar las dependencias en el ambiente: \
```pip install -r requirements.txt```
## Uso chat bot
### Crear un Bot en Telegram y Obtener el `chat_id`

### 1. Crear el Bot en Telegram
- Abre **Telegram** y busca el bot oficial llamado `BotFather`.
- Inicia una conversación con `BotFather` y utiliza el comando `/newbot`.
- Sigue las instrucciones para nombrar tu bot y asignarle un nombre de usuario. Debe terminar en `bot` (e.g., `mi_primer_bot`).
- `BotFather` te proporcionará un **token de acceso**. Guárdalo, es necesario para interactuar con la API de Telegram.

### 2. Enviar un Mensaje al Bot
- Busca tu bot en Telegram usando el nombre de usuario creado.
- Inicia una conversación enviando cualquier mensaje.

### 3. Obtener el `chat_id`
- Realiza una solicitud **HTTP GET** a la siguiente URL: `https://api.telegram.org/bot[TU_TOKEN]/getUpdates`
- Reemplaza `[TU_TOKEN]` con el token proporcionado por `BotFather`.
- La solicitud puede hacerse desde un navegador o herramientas como Postman.
- En la respuesta, localiza el campo `chat` bajo `message`, ahí encontrarás el `chat_id`.

**Nota:** El `chat_id` es único para cada conversación. 

### 4. Poner el token y el chat_id en sus respectivas variables en lineas XX y XX. 


Desde backend/models/Automatic-License-Plate-Recognition-using-YOLOv8/
- En el script network_utils.py modificar la funcion sendTelegram() para que se utilice el bot con el chat deseado
## video
Debe tenerse el video sample.mp4 que sera utilizado como si fuese una camara dentro de la carpeta: 
backend/models/Automatic-License-Plate-Recognition-using-YOLOv8/
El video utilizado para testear es:
https://drive.google.com/file/d/1JbwLyqpFCXmftaJY1oap8Sa6KfjoWJta/view?usp=sharing 

Dentro del ambiente
- Correr el Servidor:\
```python main.py```
- Correr el Cliente:\
```python client.py```
# Base de datos
## Instalacion
desde backend/database/
- Crear ambiente\
```python -m venv venv```
- Activar el ambiente\
```./env/Scripts/activate```
- Alternativamente\
```source ./venv/bin/activate```
- Instalar las dependencias en el ambiente\
```pip install -r requirements.txt```
## Uso
desde backend/database/
```uvicorn app:app```
inferfaz de fast api para probar endpoints:\
127.0.0.1:8000/docs/\
