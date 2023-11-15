import os
import time
import requests
import cv2


# import asyncio
# from telegram import Bot

# async def sendTelegram():
#     bot = Bot(token="6727869623:AAEs75zZa7-_KnVQkF9Hvl2n8MzllTeI5MM")
#     await bot.send_message(chat_id=901902380, text='OE AY TERRIBLE NAE SOSPECHOSA POR AHI CUIDAITOO')

# async def main():
#     await sendTelegram()

# if __name__ == "__main__":
#     asyncio.run(main())

url = "http://127.0.0.1:5000/detect_license_plate"

video_filename = "./images/gringo/sample.mp4"
video = cv2.VideoCapture(video_filename)

if not video.isOpened():
    print("Error: Could not open video.")
else:
    frame_count = 0
    while True:
        success, frame = video.read()
        if not success:
            break
        if frame_count % 30 == 0: #fps del video original 
            frame_filename = f"./images/toSend/frame_{frame_count}.png"
            cv2.imwrite(frame_filename, frame)

            with open(frame_filename, 'rb') as image_file:
                response = requests.post(url, files={"image": image_file})
            print(f"Sent frame {frame_count}. Server response:", response.json())
            os.remove(frame_filename)
            #time.sleep(0.5)
        frame_count += 1

    video.release()
    print("Video processing completed.")