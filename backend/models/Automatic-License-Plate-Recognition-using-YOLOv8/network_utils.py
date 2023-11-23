from concurrent.futures import ThreadPoolExecutor
import requests
import json
from datetime import datetime
import asyncio
import telegram

url = 'http://127.0.0.1:8000'


def send_license_plate_data(data):
    #Envía datos de placas de vehículos a un endpoint de API específico.
    api_endpoint = url+'/horarios' 
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print('Success:', response.json())
    except requests.exceptions.HTTPError as errh:
        print('Http Error:', errh)
    except requests.exceptions.ConnectionError as errc:
        print('Error Connecting:', errc)
    except requests.exceptions.Timeout as errt:
        print('Timeout Error:', errt)
    except requests.exceptions.RequestException as err:
        print('Error:', err)

def send_telegram_async():
    #Inicia una tarea asíncrona para enviar un mensaje a Telegram.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(sendTelegram())

def isSuspiciousBehaviour(licensePlate):
    #Evalúa si el comportamiento de una placa es sospechoso basándose en ciertos criterios.
    #Esta condicion se customiza dependiendo de la poblacion, 
        #Por defecto un auto sospechoso es aquel que se detecta por 3 camaras distintas en un rango de tiempo menor a 30 minutos
    api_endpoint = url+'/horarios/30minuteTimeRange/'+licensePlate+'/'+str(int(datetime.timestamp(datetime.now())))
    response = requests.get(api_endpoint)
    camSet = set()
    for detection in response.json():
        camSet.add(int(detection['lugar']))
    if len(camSet) >= 3:
        with ThreadPoolExecutor() as executor:
            executor.submit(send_telegram_async)
        return True
    return False
    
async def sendTelegram():
    #Función asíncrona para enviar mensajes a través de Telegram.
    #bot = telegram.Bot("") <---------------------------------------SE AGREGA TOKEN
    async with bot:
        await bot.send_message(text='Mensaje serio que incluye patente peligrosa', chat_id=901902380)

stored_horarios = []        
def cache_horarios():
    #Cachear los datos de registro de deteccion obtenidos de un endpoint de API, para detectar mas rapidamente.
    global stored_horarios
    try:
        response = requests.get(url+'/horarios')
        response.raise_for_status()
        stored_horarios = response.json()
    except requests.RequestException as e: 
        print("Error: ",e)

stored_plates = []
def cache_plates():
    #Cachear los datos de placas de vehículos registrados en la comunidad, obtenidos de un endpoint de API, para detectar mas rapidamente.
    global stored_plates
    try:
        response = requests.get(url+'/autos_plates')
        response.raise_for_status()
        stored_plates = response.json()
    except requests.RequestException as e: 
        print("Error: ",e)

def check_horarios(horario):
     #Verifica y actualiza los datos de deteccion de patente almacenados en caché.
     #Al detectar una patente se reemplaza la deteccion si se obtiene una probabilidad mas alta, en vez de registrar todas las petentes detectadas, a menos que no este registrada
    global stored_horarios
    found = False

    for stored_horario in stored_horarios:
        if stored_horario['horario'] == horario:
            found = True
            if stored_horario['probabilidad'] < horario['probabilidad']:
                try:
                    response = requests.put(url+'/horarios', json=horario)
                    response.raise_for_status()
                    stored_horario['probabilidad'] = horario['probabilidad']
                except requests.RequestException as e:
                    print("Error:", e)
            break

    if not found:
        try:
            response = requests.post(url+'/horarios', json=horario)
            response.raise_for_status()
            stored_horarios.append(horario)
        except requests.RequestException as e:
            print("Error:", e)

def check_license_plate(plate):
     #Verifica si una placa está en la caché (osea que esta registrada como de la comunidad)
    if plate in stored_plates:
        return True
    else:
        isSuspiciousBehaviour(plate)
        return False
    

