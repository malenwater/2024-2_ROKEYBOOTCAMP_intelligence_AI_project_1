import time
import serial
import requests
import numpy
from io import BytesIO
from pprint import pprint
import os

import cv2

ser = serial.Serial("/dev/ttyACM0", 9600)

# API endpoint
api_url = ""

# set path and image number
paths = "./test0"
img_max = 3

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
        if current_count >= img_max:
            print("The folder already contains the maximum number of images. Stopping.")
            break
        
        data = ser.read()
        print(data)
        
        
        if data == b"0":
            
            img = get_img()
            new_filename = os.path.join(paths, f"{current_count + 1:04d}.jpg")
            cv2.imwrite(new_filename, img)
            print(f"Image saved as: {new_filename}")
            cv2.imshow("Image", img)
            
            key = cv2.waitKey(3000)  # 3000 ms = 3 seconds
            if key == ord('q'):  # If 'q' is pressed, close the window
                cv2.destroyAllWindows()
            
            # crop_info = None
            # crop_info = {"x": 200, "y": 100, "width": 300, "height": 300}

            # if crop_info is not None:
            #     img = crop_img(img, crop_info)


            # result = inference_reqeust(img, api_url)
            ser.write(b"1")
            img_count += 1
        else:
            pass
        
if __name__ == "__main__":
    save_img()
