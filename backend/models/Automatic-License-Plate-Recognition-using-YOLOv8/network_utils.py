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

def update_license_plate_data(data):
    api_endpoint = url+'/horarios/'+str(data['car_id'])
    print("UPDATE LICENSE PLATE  " + api_endpoint)
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.put(api_endpoint, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print('Success:', response.json())
    except Exception as e:
        print(f"An error ocurred: {e}")


def delete_license_plate(car_id):
    api_endpoint = url+'/horarios/car_id/'+str(data['car_id'])
    
    try:
        response = request.delete(api_endpoint)
        response.raise_for_status()
        print('Success:', response.json())
    except Exception as e:
        print(f"An error ocurred: {e}")
    

def send_telegram_async():
    #Inicia una tarea asíncrona para enviar un mensaje a Telegram.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(sendTelegram())

def detect_suspicious_behaviour(licensePlate):
    #Evalúa si el comportamiento de una placa es sospechoso basándose en ciertos criterios.
    #Esta condicion se customiza dependiendo de la poblacion, 
        #Por defecto un auto sospechoso es aquel que se detecta por 3 camaras distintas en un rango de tiempo menor a 30 minutos
    api_endpoint = url+'/horarios/30minuteTimeRange/'+licensePlate+'/'+str(int(datetime.timestamp(datetime.now())))
    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()
        print('Success:', response.json())
        camSet = set()
        for detection in response.json():
            camSet.add(int(detection['lugar']))
        if len(camSet) >= 3:
            with ThreadPoolExecutor() as executor:
                executor.submit(send_telegram_async)
            return True
        return False
    except Exception as e:
        print(f"An error ocurred: {e}")
    
async def sendTelegram():
    #Función asíncrona para enviar mensajes a través de Telegram.
    #bot = telegram.Bot("") <---------------------------------------SE AGREGA TOKEN
    async with bot:
        await bot.send_message(text='Mensaje serio que incluye patente peligrosa', chat_id=901902380)

stored_horarios = {} 
def cache_horarios():
    #Cachear los datos de registro de deteccion obtenidos de un endpoint de API, para detectar mas rapidamente.
    global stored_horarios
    try:
        response = requests.get(url+'/horarios')
        response.raise_for_status()
        horarios = response.json()
        for horario in horarios:
            stored_horarios[horario['car_id']] = [horario['licence'],horario['probability']]
    except requests.RequestException as e: 
        print("Error: ",e)


stored_community_plates = []
def cache_plates():
    #Cachear los datos de placas de vehículos registrados en la comunidad, obtenidos de un endpoint de API, para detectar mas rapidamente.
    global stored_community_plates
    try:
        response = requests.get(url+'/autos_plates')
        response.raise_for_status()
        stored_community_plates = response.json()
    except requests.RequestException as e: 
        print("Error: ",e)

def process_new_car_id(detection_data):
    global stored_community_plates
    global stored_horarios
    car_id = detection_data['car_id']
    license_plate = detection_data['licence']
    confidence = detection_data['probability']
    #Se guarda en el cache, se revisa si la placa es de la comunidad
    #en caso de no ser de la comunidad se envia la informacion a la BD y se revisa posible comportamiento sospechoso
    stored_horarios[car_id] = [license_plate, confidence]
    if license_plate in stored_community_plates:
        return
    send_license_plate_data(detection_data)
    detect_suspicious_behaviour(license_plate)


def process_known_car_id(detection_data):
    global stored_community_plates
    global stored_horarios
    car_id = detection_data['car_id']
    license_plate = detection_data['licence']
    confidence = detection_data['probability']

    #si la confianza(probability) cacheada es mayor a la nueva deteccion, detenemos ejecucion(peor prediccion a la guardada)
    if confidence <= stored_horarios[car_id][1]:
        return

    #si encuentra la misma placa con mayor confianza se actualiza la confianza en cache
    if license_plate == stored_horarios[car_id][0]:
        stored_horarios[car_id][1] = confidence
        return

    #En caso de que la nueva lectura de esta id es parte de la comunidad se elimina el registro de la BD
    if license_plate in stored_community_plates:
        if stored_horarios[car_id][0] not in stored_community_plates:
            delete_license_plate(car_id)
        stored_horarios[car_id] = [license_plate, confidence]
        return

    #No estaba antes en BD
    if stored_horarios[car_id][0] in stored_community_plates:
        send_license_plate_data(detection_data)
    else:
        update_license_plate_data(detection_data)   
    detect_suspicious_behaviour(license_plate)
    stored_horarios[car_id] = [license_plate, confidence]

    

def process_detection(detection_data):
    global stored_horarios
    car_id = detection_data['car_id']
    #si el id de deteccion no existe en el cache
    if(car_id not in stored_horarios):
        process_new_car_id(detection_data)
    else:
        process_known_car_id(detection_data)

    


    