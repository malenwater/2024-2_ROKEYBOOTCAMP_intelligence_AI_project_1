import requests
from requests.auth import HTTPBasicAuth
import cv2
"""_summary_
    해당 파이썬 파일은 단일 파일로, 본 프로젝트에서 라즈베리파이에 연결된 카메라와 센서를 통해서 얻은 이미지를,
    superbai 의 ai 모델에 집어넣어서 본 프로젝트에 맞는 class 정보에 따른 바운딩 박스를 친 이미지를 open cv를 통해 확인 가능한 파일
    paths : 저장할 폴더 이름
    img_name : 저장할 이미지 앞 이름
    img_max : 저장할 이미지 개수
"""
URL = "superbAI's URL"
ACCESS_KEY = "superbAI's team key"
IMAGE_FILE_PATH = "E:\\study\\2024-2_ROKEYBOOTCAMP_intelligence_AI_project_1\\dataset\\dectect\\data\\test_val_1_0001.jpg"

image = open(IMAGE_FILE_PATH, "rb").read()
item_color_map = {
    "RASPBERRY PICO": (255, 0, 0),
    "HOLE": (0, 255, 0),
    "BOOTSEL": (0, 0, 255),
    "OSCILLATOR": (255, 255, 0),
    "USB": (0, 255, 255),
    "CHIPSET": (255, 0, 255)
}
def solove_model(URL,ACCESS_KEY,image):
    response = requests.post(
        url=URL,
        auth=HTTPBasicAuth("kdt2025_1-22", ACCESS_KEY),
        headers={"Content-Type": "image/jpeg"},
        data=image,
    )
    print("end model")
    return response.json()
def show_img(img_path,response):
    img = cv2.imread(img_path)
    # print(img)
    print(response)
    for one_data in response['objects']:
        # 이미지 파일 경로 설정
        # 박스 칠 좌표 설정 (예: 좌측 상단 (50, 50), 우측 하단 (200, 200))
        start_point = (one_data['box'][0], one_data['box'][1]) # 박스 시작 좌표 (x, y)
        end_point = (one_data['box'][2], one_data['box'][3]) # 박스 끝 좌표 (x, y)
        color = item_color_map.get(one_data['class'], (255, 255, 255))
        thickness = 2 # 박스 선의 두께
        # 박스 그리기
        cv2.rectangle(img, start_point, end_point, color, thickness)
        # 텍스트 설정
        text = one_data['class'] + " : "+ str(one_data['score'])# 추가할 텍스트
        position = (one_data['box'][0], one_data['box'][1]) # 텍스트 시작 위치 (x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX # 글꼴 설정
        font_scale = 0.5 # 글자 크기
        color = (0, 255, 0) # BGR 색상 (초록색)
        thickness = 2 # 글자 두께
        # 텍스트 추가
        cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
    print("show model")
    cv2.imshow('Window Name_1', img)
    cv2.waitKey(20000)
    cv2.destroyAllWindows()
response = solove_model(URL,ACCESS_KEY,image)
show_img(IMAGE_FILE_PATH,response)