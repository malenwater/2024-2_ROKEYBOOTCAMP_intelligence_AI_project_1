import requests
from requests.auth import HTTPBasicAuth
import cv2
import os
import json
"""_summary_
    해당 파일은 아래 jpg_files의 jpg를 superbai의 url에 넣어서 결과를 나오도록 하는 파일이다.
    result_path : 비교할 txt를 저장할 위치
    all_result_path : 기타 정보인 img, json 파일을 저장할 위치
"""
URL = "subperbAI의 모델 URL"
ACCESS_KEY = "subperbAI 팀 키"
result_path = "./results/small_model/result"
all_result_path = "./results/small_model/all_result"

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
    print(img)
    for one_data in response['objects']:
        # 이미지 파일 경로 설정
        # 박스 칠 좌표 설정 (예: 좌측 상단 (50, 50), 우측 하단 (200, 200))
        start_point = (one_data['box'][0], one_data['box'][1]) # 박스 시작 좌표 (x, y)
        end_point = (one_data['box'][2], one_data['box'][3]) # 박스 끝 좌표 (x, y)
        color = (0, 255, 0) # BGR 색상 (초록색)
        thickness = 2 # 박스 선의 두께
        # 박스 그리기
        cv2.rectangle(img, start_point, end_point, color, thickness)
        # 텍스트 설정
        text = one_data['class'] + " : "+ str(one_data['score'])# 추가할 텍스트
        position = (one_data['box'][0], one_data['box'][1]) # 텍스트 시작 위치 (x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX # 글꼴 설정
        font_scale = 1 # 글자 크기
        color = (0, 255, 0) # BGR 색상 (초록색)
        thickness = 2 # 글자 두께
        # 텍스트 추가
        cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
    print("show model")
    cv2.imshow('Window Name_1', img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# 모든 .jpg 파일 경로를 리스트로 저장
jpg_files = ['./test_val_1/test_val_1_0001.jpg', './test_val_1/test_val_1_0002.jpg', 
 './test_val_1/test_val_1_0003.jpg', './test_val_1/test_val_1_0004.jpg', 
 './test_val_1/test_val_1_0005.jpg', './test_val_1/test_val_1_0006.jpg', 
 './test_val_1/test_val_1_0007.jpg', './test_val_1/test_val_1_0008.jpg', 
 './test_val_2_1/test_val_2_1_0001.jpg', './test_val_2_1/test_val_2_1_0002.jpg', 
 './test_val_2_1/test_val_2_1_0003.jpg', './test_val_2_1/test_val_2_1_0004.jpg',
 './test_val_2_1/test_val_2_1_0005.jpg', './test_val_2_1/test_val_2_1_0006.jpg',
 './test_val_2_1/test_val_2_1_0007.jpg', './test_val_2_1/test_val_2_1_0008.jpg',
 './test_val_2_2/test_val_2_2_0001.jpg', './test_val_2_2/test_val_2_2_0002.jpg',
 './test_val_2_2/test_val_2_2_0003.jpg', './test_val_2_2/test_val_2_2_0004.jpg',
 './test_val_2_2/test_val_2_2_0005.jpg', './test_val_2_2/test_val_2_2_0006.jpg',
 './test_val_2_2/test_val_2_2_0007.jpg', './test_val_2_2/test_val_2_2_0008.jpg',
 './test_val_2_3/test_val_2_3_0001.jpg', './test_val_2_3/test_val_2_3_0002.jpg',
 './test_val_2_3/test_val_2_3_0003.jpg', './test_val_2_3/test_val_2_3_0004.jpg',
 './test_val_2_3/test_val_2_3_0005.jpg', './test_val_2_3/test_val_2_3_0006.jpg',
 './test_val_2_3/test_val_2_3_0007.jpg', './test_val_2_3/test_val_2_3_0008.jpg',
 './test_val_2_4/test_val_2_4_0001.jpg', './test_val_2_4/test_val_2_4_0002.jpg',
 './test_val_2_4/test_val_2_4_0003.jpg', './test_val_2_4/test_val_2_4_0004.jpg',
 './test_val_2_4/test_val_2_4_0005.jpg', './test_val_2_4/test_val_2_4_0006.jpg',
 './test_val_2_4/test_val_2_4_0007.jpg', './test_val_2_4/test_val_2_4_0008.jpg',
 './test_val_2_5/test_val_2_5_0001.jpg', './test_val_2_5/test_val_2_5_0002.jpg',
 './test_val_2_5/test_val_2_5_0003.jpg', './test_val_2_5/test_val_2_5_0004.jpg',
 './test_val_2_5/test_val_2_5_0005.jpg', './test_val_2_5/test_val_2_5_0006.jpg',
 './test_val_2_5/test_val_2_5_0007.jpg', './test_val_2_5/test_val_2_5_0008.jpg',
 './test_val_2_6/test_val_2_6_0001.jpg', './test_val_2_6/test_val_2_6_0002.jpg',
 './test_val_2_6/test_val_2_6_0003.jpg', './test_val_2_6/test_val_2_6_0004.jpg',
 './test_val_2_6/test_val_2_6_0005.jpg', './test_val_2_6/test_val_2_6_0006.jpg',
 './test_val_2_6/test_val_2_6_0007.jpg', './test_val_2_6/test_val_2_6_0008.jpg',
 './test_val_3_1/test_val_3_1_0001.jpg', './test_val_3_1/test_val_3_1_0002.jpg',
 './test_val_3_1/test_val_3_1_0003.jpg', './test_val_3_1/test_val_3_1_0004.jpg',
 './test_val_3_1/test_val_3_1_0005.jpg', './test_val_3_1/test_val_3_1_0006.jpg',
 './test_val_3_1/test_val_3_1_0007.jpg', './test_val_3_1/test_val_3_1_0008.jpg',
 './test_val_3_2/test_val_3_2_0001.jpg', './test_val_3_2/test_val_3_2_0002.jpg',
 './test_val_3_2/test_val_3_2_0003.jpg', './test_val_3_2/test_val_3_2_0004.jpg',
 './test_val_3_2/test_val_3_2_0005.jpg', './test_val_3_2/test_val_3_2_0006.jpg',
 './test_val_3_2/test_val_3_2_0007.jpg', './test_val_3_2/test_val_3_2_0008.jpg',
 './test_val_3_3/test_val_3_3_0001.jpg', './test_val_3_3/test_val_3_3_0002.jpg',
 './test_val_3_3/test_val_3_3_0003.jpg', './test_val_3_3/test_val_3_3_0004.jpg',
 './test_val_3_3/test_val_3_3_0005.jpg', './test_val_3_3/test_val_3_3_0006.jpg',
 './test_val_3_3/test_val_3_3_0007.jpg', './test_val_3_3/test_val_3_3_0008.jpg',
 './test_val_3_4/test_val_3_4_0001.jpg', './test_val_3_4/test_val_3_4_0002.jpg',
 './test_val_3_4/test_val_3_4_0003.jpg', './test_val_3_4/test_val_3_4_0004.jpg',
 './test_val_3_4/test_val_3_4_0005.jpg', './test_val_3_4/test_val_3_4_0006.jpg',
 './test_val_3_4/test_val_3_4_0007.jpg', './test_val_3_4/test_val_3_4_0008.jpg',
 './test_val_3_5/test_val_3_5_0001.jpg', './test_val_3_5/test_val_3_5_0002.jpg',
 './test_val_3_5/test_val_3_5_0003.jpg', './test_val_3_5/test_val_3_5_0004.jpg',
 './test_val_3_5/test_val_3_5_0005.jpg', './test_val_3_5/test_val_3_5_0006.jpg',
 './test_val_3_5/test_val_3_5_0007.jpg', './test_val_3_5/test_val_3_5_0008.jpg', 
 './test_val_3_6/test_val_3_6_0001.jpg', './test_val_3_6/test_val_3_6_0002.jpg', 
 './test_val_3_6/test_val_3_6_0003.jpg', './test_val_3_6/test_val_3_6_0004.jpg', 
 './test_val_3_6/test_val_3_6_0005.jpg', './test_val_3_6/test_val_3_6_0006.jpg', 
 './test_val_3_6/test_val_3_6_0007.jpg', './test_val_3_6/test_val_3_6_0008.jpg', 
 './test_val_4_1/test_val_4_1_0001.jpg', './test_val_4_1/test_val_4_1_0002.jpg', 
 './test_val_4_1/test_val_4_1_0003.jpg', './test_val_4_1/test_val_4_1_0004.jpg', 
 './test_val_4_1/test_val_4_1_0005.jpg', './test_val_4_1/test_val_4_1_0006.jpg', 
 './test_val_4_1/test_val_4_1_0007.jpg', './test_val_4_1/test_val_4_1_0008.jpg', 
 './test_val_4_2/test_val_4_2_0001.jpg', './test_val_4_2/test_val_4_2_0002.jpg', 
 './test_val_4_2/test_val_4_2_0003.jpg', './test_val_4_2/test_val_4_2_0004.jpg', 
 './test_val_4_2/test_val_4_2_0005.jpg', './test_val_4_2/test_val_4_2_0006.jpg', 
 './test_val_4_2/test_val_4_2_0007.jpg', './test_val_4_2/test_val_4_2_0008.jpg', 
 './test_val_5_1/test_val_5_1_0001.jpg', './test_val_5_1/test_val_5_1_0002.jpg', 
 './test_val_5_1/test_val_5_1_0003.jpg', './test_val_5_1/test_val_5_1_0004.jpg', 
 './test_val_5_1/test_val_5_1_0005.jpg', './test_val_5_1/test_val_5_1_0006.jpg', 
 './test_val_5_2/test_val_5_2_0001.jpg', './test_val_5_2/test_val_5_2_0002.jpg', 
 './test_val_5_2/test_val_5_2_0003.jpg', './test_val_5_2/test_val_5_2_0004.jpg', 
 './test_val_5_2/test_val_5_2_0005.jpg', './test_val_5_2/test_val_5_2_0006.jpg', 
 './test_val_6_1/test_val_6_1_0001.jpg', './test_val_6_1/test_val_6_1_0002.jpg', 
 './test_val_6_1/test_val_6_1_0003.jpg', './test_val_6_1/test_val_6_1_0004.jpg', 
 './test_val_6_2/test_val_6_2_0001.jpg', './test_val_6_2/test_val_6_2_0002.jpg', 
 './test_val_6_2/test_val_6_2_0003.jpg', './test_val_6_2/test_val_6_2_0004.jpg', 
 './test_val_7_1/test_val_7_1_0001.jpg', './test_val_7_1/test_val_7_1_0002.jpg', 
 './test_val_7_1/test_val_7_1_0003.jpg', './test_val_7_1/test_val_7_1_0004.jpg', 
 './test_val_7_2/test_val_7_2_0001.jpg', './test_val_7_2/test_val_7_2_0002.jpg', 
 './test_val_7_2/test_val_7_2_0003.jpg', './test_val_7_2/test_val_7_2_0004.jpg', 
 './test_val_8/test_val_8_0001.jpg', './test_val_8/test_val_8_0002.jpg',
 './test_val_8/test_val_8_0003.jpg', './test_val_8/test_val_8_0004.jpg',
 './test_val_8/test_val_8_0005.jpg', './test_val_8/test_val_8_0006.jpg',
 './test_val_8/test_val_8_0007.jpg', './test_val_8/test_val_8_0008.jpg']

item_color_map = {
    "RASPBERRY PICO": (255, 0, 0),    # 빨간색
    "HOLE": (0, 255, 0),             # 초록색
    "BOOTSEL": (0, 0, 255),          # 파란색
    "OSCILLATOR": (255, 255, 0),     # 노란색
    "USB": (0, 255, 255),            # 청록색
    "CHIPSET": (255, 0, 255)         # 보라색
}


os.makedirs(result_path, exist_ok=True)
os.makedirs(all_result_path, exist_ok=True)

def save_result(img_path,response):
    # 이미지 파일 이름 추출
    img_filename = os.path.basename(img_path)

    # 이미지 이름에 .txt 확장자를 붙여 JSON 파일 이름 생성
    txt_filename = f"{os.path.splitext(img_filename)[0]}.txt"
    txt_filepath = os.path.join(result_path, txt_filename)
    class_counts = {
        "RASPBERRY PICO" : 0,
        "OSCILLATOR" : 0,
        "HOLE" : 0,
        "USB" : 0,
        "BOOTSEL" : 0,
        "CHIPSET" : 0,
    }
    # print(txt_filepath)
    # pass 또는 deny 결정 (여기서는 예시로 객체의 score 값에 따라 판단)
    # 예를 들어, score 값이 0.5 이상이면 'pass', 그렇지 않으면 'deny'
    status = "pass" if any(obj['score'] >= 0.5 for obj in response['objects']) else "deny"
    for one_data in response['objects']:
        # print(one_data)
        class_name = one_data['class']
        class_counts[class_name] = class_counts.get(class_name, 0) + 1
        
    hole_count = class_counts.get("HOLE", 0)
    other_counts = {key: value for key, value in class_counts.items() if key != "HOLE"}
    
    
    if hole_count == 4 and all(count == 1 for count in other_counts.values()):
        status = "pass"
    else:
        status = "deny"
        
    # # 파일에 'pass' 또는 'deny' 값 쓰기
    try:
        with open(txt_filepath, 'w') as file:
            file.write(status)
        print(f"Result saved in {txt_filepath}: {status}")
    except Exception as e:
        print(f"Error saving result: {e}")
    
def save_all_result(img_path,response):
    # 이미지 경로에서 파일 이름 추출
    img_filename = os.path.basename(img_path)

    # 이미지 이름에 .json 확장자를 붙여 JSON 파일 이름 생성
    json_filename = f"{os.path.splitext(img_filename)[0]}.json"
    json_filepath = os.path.join(all_result_path, json_filename)

    # response를 JSON으로 저장
    try:
        with open(json_filepath, 'w') as json_file:
            json.dump(response, json_file, indent=4)
        # print(f"Result saved for {img_filename} at {json_filepath}")
    except Exception as e:
        print(f"Error saving result for {img_filename}: {e}")
        
def save_image(img_path,response):
    img_filename = os.path.basename(img_path)
    all_img_filepath = os.path.join(all_result_path, img_filename)
    # print(img_path)
    # print(all_img_filepath)
    
    img = cv2.imread(img_path)
    for one_data in response['objects']:
        # 이미지 파일 경로 설정
        # 박스 칠 좌표 설정 (예: 좌측 상단 (50, 50), 우측 하단 (200, 200))
        start_point = (one_data['box'][0], one_data['box'][1]) # 박스 시작 좌표 (x, y)
        end_point = (one_data['box'][2], one_data['box'][3]) # 박스 끝 좌표 (x, y)
        color = item_color_map[one_data['class']] # BGR 색상 (초록색)
        thickness = 2 # 박스 선의 두께
        # 박스 그리기
        cv2.rectangle(img, start_point, end_point, color, thickness)
        
        # 텍스트 설정 = 원하면 text를 적어놓아서 저장 가능
        # text = one_data['class']# + " : "+ str(one_data['score'])    # 추가할 텍스트
        # position = (one_data['box'][0] - 20, one_data['box'][1] - 10) # 텍스트 시작 위치 (x, y)
        # font = cv2.FONT_HERSHEY_SIMPLEX # 글꼴 설정
        # font_scale = 0.5 # 글자 크기
        # color = item_color_map[one_data['class']] # BGR 색상 (초록색)
        # thickness = 2 # 글자 두께
        # # 텍스트 추가
        # cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
        
        
    # print(" model")
    cv2.imwrite(all_img_filepath, img)


for img_path in jpg_files:
    image = open(img_path, "rb").read()
    response = solove_model(URL,ACCESS_KEY,image)
    # print(response)
    save_result(img_path,response)
    save_all_result(img_path,response)
    save_image(img_path,response)
    # break
    # show_img(IMAGE_FILE_PATH,response)
print("end_evalaute")
