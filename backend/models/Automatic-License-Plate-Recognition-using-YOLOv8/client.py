import os
import time
import requests
import cv2

# Simulacion de camara como cliente, que envia fotografias en vivo 
url = "http://127.0.0.1:5000/detect_license_plate"

video_filename = "./sample.mp4"
video = cv2.VideoCapture(video_filename)

if not video.isOpened():
    print("Error: Could not open video.")                                               # Verifica si el video se pudo abrir correctamente.
else:
    frame_count = 0
    while True:
        success, frame = video.read()
        if not success:                                                                 # Sale del bucle si no puede leer más fotogramas.
            break
        if frame_count % 30 == 0:                                                       # Procesa un fotograma cada 30 para coincidir con la mitad de los fps del video.
            frame_filename = f"./images/toSend/frame_{frame_count}.png"                 # Guarda el fotograma como imagen PNG.
            cv2.imwrite(frame_filename, frame)

            with open(frame_filename, 'rb') as image_file:                              # Envía la imagen del fotograma al servidor para la detección de placas.
                response = requests.post(url, files={"image": image_file})              # Elimina el archivo de imagen después de enviarlo.
            print(f"Sent frame {frame_count}. Server response:", response.json())      
            os.remove(frame_filename)
            #time.sleep(0.5)
        frame_count += 1

    video.release()                                                                     # Libera el recurso de video después de procesar todos los fotogramas.
    print("Video processing completed.")