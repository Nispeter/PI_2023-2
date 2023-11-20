# Modelo
## Instalacion 
desde backend/models/Automatic-License-Plate-Recognition-using-YOLOv8/
- Crear un ambiente con python=3.8:\
```conda create --prefix ./env python==3.8 -y```
- Instalar las dependencias en el ambiente: \
```pip install -r requirements.txt```
## Uso
Luego dentro del ambiente
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