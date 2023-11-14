import requests
import json
from datetime import datetime

url = 'http://127.0.0.1:8000'

def send_license_plate_data(data):
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

def isSuspiciousBehaviour(licensePlate):
    api_endpoint = url+'/horarios/30minuteTimeRange/'+licensePlate+'/'+str(int(datetime.timestamp(datetime.now())))
    response = requests.get(api_endpoint)
    camSet = set()
    for detection in response.json():
        camSet.add(int(detection['lugar']['cam_id']))
    
stored_plates = []
def cache_plates():
    global stored_plates
    try:
        response = requests.get(url+'/autos_plates')
        response.raise_for_status()
        stored_plates = response.json()
    except requests.RequestException as e: 
        print("Error: ",e)

def check_license_plate(plate):
    if plate in stored_plates:
        return True
    else:
        #isSuspiciousBehaviour(plate)
        return False