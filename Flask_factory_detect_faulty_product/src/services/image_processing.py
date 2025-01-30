import cv2
import numpy as np

def draw_chip_Labeling1(image_bytes, response,score):
    item_color_map = {
        "RASPBERRY PICO": (255, 0, 0),
        "HOLE": (0, 255, 0),
        "BOOTSEL": (0, 0, 255),
        "OSCILLATOR": (255, 255, 0),
        "USB": (0, 255, 255),
        "CHIPSET": (255, 0, 255)
    }
    
    image = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    class_confidence_text = ""

    for obj in response['objects']:
        if obj['score'] < score:
            continue
        start_point = (obj['box'][0], obj['box'][1])
        end_point = (obj['box'][2], obj['box'][3])
        color = item_color_map.get(obj['class'], (255, 255, 255))
        thickness = 2
        cv2.rectangle(img, start_point, end_point, color, thickness)
        class_confidence_text += f"{obj['class']} : {round(obj['score'], 4)}\n"

    ret, buffer = cv2.imencode('.jpg', img)
    return buffer.tobytes(), class_confidence_text if ret else ValueError("이미지 인코딩 실패")

def draw_chip_Labeling2(image_bytes, response,score):
    item_color_map = {
        "Broken": (255, 0, 0),
        "Nomal": (0, 255, 0),
        "broken": (255, 0, 0),
        "nomal": (0, 255, 0),
    }
    
    image = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    class_confidence_text = ""

    for obj in response['objects']:
        if obj['score'] < score:
            continue
        start_point = (obj['box'][0], obj['box'][1])
        end_point = (obj['box'][2], obj['box'][3])
        color = item_color_map.get(obj['class'], (255, 255, 255))
        thickness = 2
        cv2.rectangle(img, start_point, end_point, color, thickness)
        class_confidence_text += f"{obj['class']} : {round(obj['score'], 4)}\n"

    ret, buffer = cv2.imencode('.jpg', img)
    return buffer.tobytes(), class_confidence_text if ret else ValueError("이미지 인코딩 실패")

def check_chip_nomal(response1,response2,score):
    check_component = ""
    check_nomal = ""
    # check component
    class_counts = {
        "RASPBERRY PICO": 0,
        "OSCILLATOR": 0,
        "HOLE": 0,
        "USB": 0,
        "BOOTSEL": 0,
        "CHIPSET": 0,
    }
    status = "pass"  # 기본값을 "pass"로 설정
    for one_data in response1['objects']:
        # score가 0.8 이상인 경우에만 처리
        if one_data['score'] >= score:
            class_name = one_data['class']
            # class_name이 class_counts에 있다면 count를 증가시킴
            if class_name in class_counts:
                class_counts[class_name] += 1

    # HOLE 개수 확인
    hole_count = class_counts.get("HOLE", 0)

    # HOLE을 제외한 다른 클래스들의 개수 확인
    other_counts = {key: value for key, value in class_counts.items() if key != "HOLE"}
    # 조건에 맞게 status 결정
    if hole_count == 4 and all(count == 1 for count in other_counts.values()):
        status = "pass"
    else:
        status = "deny"
        
    if status == "pass":
        check_component += f"정상품 :  {score}이상의 신뢰성으로 칩의 모든 구성요소가 있습니다."
    elif status == "deny":
        check_component += f"불량품 :  {score}이상의 신뢰성으로 칩의 구성요소 중 몇개가 없습니다."
    
    # check nomal
    if len(response2['objects']) == 1:
        one_data = response2['objects'][0]
        if one_data['class'] == "Nomal" or one_data['class'] == "nomal" and one_data['score'] >= score:
            check_nomal += f"정상품 : {score}이상의 신뢰성으로 정상품입니다."
        elif one_data['class'] == "Broken" or one_data['class'] == "broken" and one_data['score'] >= score:
            check_nomal += f"불량품 : {score}이상의 신뢰성으로 불량품입니다."
        else:
            check_nomal += f"비정상 : {score}이하의 신뢰성으로 불량품을 판단할 수 없습니다."
            
    else:
        check_nomal += "비정상 : 객체가 없거나 2개 이상의 객체를 확인하였습니다."
    
    return check_component, check_nomal