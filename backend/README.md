# Modelo
## Instalacion 
desde backend/models/
- Crear un ambiente con python=3.8:\
```conda create --prefix ./env python==3.8 -y```
- Instalar las dependencias: \
```pip install -r requirements.txt```
## Uso
Luego de tener el ambiente activado y las dependencias activadas 
- Correr el Servidor:\
```python main.py```
- Correr el Cliente:\
```python client.py```
# Base de datos
## Instalacion
```python -m venv python=3.11.4 venv```
```./env/Scripts/activate```
alternativamente\
```source ./venv/bin/activate```
```pip install -r requirements.txt```
## Uso
desde backend/database/\
```uvicorn app:app```
inferfaz de fast api para probar endpoints:\
127.0.0.1:8000/docs/\