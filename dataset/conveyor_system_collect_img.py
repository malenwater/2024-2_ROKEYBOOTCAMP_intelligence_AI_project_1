import time
import serial
import requests
import numpy
from io import BytesIO
from pprint import pprint
import os

import cv2

ser = serial.Serial("/dev/ttyACM0", 9600)
"""_summary_
    해당 파이썬 파일은 단일 파일로, 본 프로젝트에서 라즈베리파이에 연결된 카메라와 센서를 통해서 센서 앞을 칩(기판)이 지나갈 경우, 촬영하여 저장되도록한다.
    paths : 저장할 폴더 이름
    img_name : 저장할 이미지 앞 이름
    img_max : 저장할 이미지 개수
"""
# API endpoint
api_url = ""

paths = "./test_val_8"
img_name = "test_val_8"
img_max = 8


def get_img():
    """Get Image From USB Camera

    Returns:
        numpy.array: Image numpy array
    """

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Camera Error")
        exit(-1)

    ret, img = cam.read()
    cam.release()

    return img


def crop_img(img, size_dict):
    x = size_dict["x"]
    y = size_dict["y"]
    w = size_dict["width"]
    h = size_dict["height"]
    img = img[y : y + h, x : x + w]
    return img


def inference_reqeust(img: numpy.array, api_rul: str):
    """_summary_

    Args:
        img (numpy.array): Image numpy array
        api_rul (str): API URL. Inference Endpoint
    """
    _, img_encoded = cv2.imencode(".jpg", img)

    # Prepare the image for sending
    img_bytes = BytesIO(img_encoded.tobytes())

    # Send the image to the API
    files = {"file": ("image.jpg", img_bytes, "image/jpeg")}

    print(files)

    try:
        response = requests.post(api_url, files=files)
        if response.status_code == 200:
            pprint(response.json())
            return response.json()
            print("Image sent successfully")
        else:
            print(f"Failed to send image. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")

def save_img():
    if not os.path.exists(paths):
        os.makedirs(paths)
        print("Folder created:", paths)
    else:
        print("Folder already exists:", paths)
    jpg_files = [f for f in os.listdir(paths) if f.endswith('.jpg')]
    current_count = len(jpg_files)
    print("Current number of .jpg files:", current_count)
    
    while 1:
        print("current_count and img_max",current_count,img_max)
        if current_count >= img_max:
            print("The folder already contains the maximum number of images. Stopping.")
            break
        
        data = ser.read()
        print(data)
        
        
        if data == b"0":
            
            img = get_img()
            new_filename = os.path.join(paths, f"{img_name}_{current_count + 1:04d}.jpg")

            crop_info = {"x": 250, "y": 130, "width": 256, "height": 256}

            if crop_info is not None:
                img = crop_img(img, crop_info)

            cv2.imwrite(new_filename, img)
            print(f"Image saved as: {new_filename}")

            # Text to display
            text = str(current_count + 1)

            # Font settings
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            font_color = (0, 0, 255)  # White text
            thickness = 2
            line_type = cv2.LINE_AA

            # Position of the text (top-left corner)
            position = (10, 30)  # (x, y)

            # Write the text on the image
            cv2.putText(img, text, position, font, font_scale, font_color, thickness, line_type)

            cv2.imshow("Image", img)
            
            key = cv2.waitKey(1000)  # 3000 ms = 3 seconds
            if key == ord('q'):  # If 'q' is pressed, close the window
                cv2.destroyAllWindows()
            current_count += 1

            if current_count >= img_max:
                print("The folder already contains the maximum number of images. Stopping.")
                break
                
            ser.write(b"1")
        else:
            pass
        
if __name__ == "__main__":
    save_img()