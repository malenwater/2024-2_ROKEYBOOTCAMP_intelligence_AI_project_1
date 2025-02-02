import time # 시간 관련 작업(현재는 사용 X)
import serial # 직렬 통신
import requests # HTTP 요청을 보내기 위함(API 호출)
import numpy # 이미지 데이터 처리를 위함
from io import BytesIO # 메모리 상에서 바이너리 데이터(이미지)를 처리하기 위함
from pprint import pprint # JSON 데이터를 보기 좋게 출력하기 위함
import cv2 # OpenCV 라이브러리로 이미지 캡쳐 및 처리를 위함
import os # 파일 및 디렉터리 관련 작업(경로 생성)등을 처리하기 위함

# 직렬 통신
ser = serial.Serial("/dev/ttyACM0", 9600)

# API endpoint
api_url = ""

# 이미지 저장 경로 설정
good_product_path = "./images/good/"
bad_product_path = "./images/bad/"

# 이미지 저장 폴더 생성
os.makedirs(good_product_path, exist_ok=True)
os.makedirs(bad_product_path, exist_ok=True)


# 이미지 캡쳐 함수
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


# 이미지 자르기 함수
def crop_img(img, size_dict):
    x = size_dict["x"]
    y = size_dict["y"]
    w = size_dict["width"]
    h = size_dict["height"]
    img = img[y : y + h, x : x + w]
    return img


# API 요청 함수(inference_request)
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


# 메인 루프
while 1:
    # 직렬 통신에서 데이터 읽기
    data = ser.read()
    print(f"Serial Data: {data}")

    if data == b"0":
        # 이미지 캡쳐
        img = get_img()

        # 이미지 크롭(필요 시)
        crop_info = {"x": 200, "y": 100, "width": 300, "height": 300}
        if crop_info is not None:
            img = crop_img(img, crop_info)

        # API로 분석 요청
        result = inference_reqeust(img, api_url)

        # 이미지 양품 / 불량품 판별 루프
        if result is not None:
                    # 예: API에서 {"status": "good"} 또는 {"status": "bad"} 반환
                    status = result.get("status", "unknown")

                    # 현재 시간으로 파일명 설정
                    timestamp = time.strftime("%Y%m%d_%H%M%S")
                    filename = f"{timestamp}.jpg"

                    if status == "good":
                        # 양품으로 저장
                        save_path = os.path.join(good_product_path, filename)
                        print(f"Saving good product to {save_path}")
                    elif status == "bad":
                        # 불량품으로 저장
                        save_path = os.path.join(bad_product_path, filename)
                        print(f"Saving bad product to {save_path}")
                    else:
                        print("Unknown status, skipping save.")
                        continue


        cv2.imwrite(save_path, img)
        cv2.imshow("", img)
        cv2.waitKey(1)
        result = inference_reqeust(img, api_url)
        ser.write(b"1")
    else:
        pass
