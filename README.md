# 2024-2_ROKEYBOOTCAMP_intelligence_AI_project_1
  - 2025/01/22~2025/01/31, 설날을 포함, 약 10일 동안 진행한 프로젝트이다.
  - 컨테이너 기반 칩(기판) 불량 시스템 구축이 프로젝트의 주제이다.

## 첫번째 프로젝트(예시)
  - 칩의 구성용품 라벨링 프로젝트

| 주제                 | 내용                                                         |
|-----------------------|-------------------------------------------------------------|
| Data Type            | Image(jpg)                                                  |
| Data Amount          | 132장, 배치 1 : 66 장, 배치 2 : 66장                        |
| Expected Labeling Unit per Data | 0 ~ 9개                                              |
| Brief Description    | 주어진 이미지에서 객체를 bounding box 하는것 - 칩의 구성요소를 파악하는 bounding box 진행하기 |
| 종료 희망 날짜        | - 배치 1 : ~2025-1-22까지, - 배치 2 : ~ 2025-1-22까지       |
| Customer Guideline   | ![Screenshot from 2025-01-22 14-28-14](https://github.com/user-attachments/assets/1e5a0b7c-62d5-4dc1-bd51-251a0c3bae7d) </br>빨간색 : RASPBERRY PICO , 주황색 : HOLE, 노란색 : BOOTSEL, 연두색 : OSCILLATOR, 파란색 : USB, 보라색 : CHIPSET|
| Data Collection      | 강사님 제공 데이터                                           |
| Annotation Type      | Bounding Box : 6종                                          |
| Class                | 1. RASPBERRY PICO, 2. HOLE, 3. BOOTSEL, 4. OSCILLATOR, 5. USB, 6. CHIPSET |
| Property             | 없음                                                        |
| Misc                 | 칩이 사진에 짤리거나 컨테이너 바깥쪽에 걸쳐서 구성용품이 짤릴 경우 구성용품의 50프로 이상이 보일 경우, 바운딩 박스를 한다. 주변이 너무 하얗거나 너무 어두워서 edge가 흐려져서 1면만 있을 경우, bounding box를 하지 않는다. 또한 bounding box를 할 때 최대한 여백을 주지 않는다. USB는 RASPBERRY PICO에 포함한다. |
|Contact Info|이선우,김영수,한건희,최범석|

|class                      |Annotation type          |부가설명                    |
|--------------------------|--------------------------|--------------------------|
|RASPBERRY PICO|Bounding Box|전체 칩 모형|
|HOLE          |Bounding Box|칩을 고정할 수 있는 4개의 핀|
|BOOTSEL        |Bounding Box|부트시 필요한 데이터를 저장하는 메로리|
|OSCILLATOR      |Bounding Box|주기 신호를 생성하는 칩|
|USB            |Bounding Box|USB를 연결할 수 있는 단자|
|CHIPSET        |Bounding Box|주요 구성 요소들 간의 데이터 흐름을 관리하는 칩셋이다|

- 특이사항 : 부품 고장을 라벨링 안하는 이유는 데이터셋에 고장이 났다는 표시나 이미지를 확인할 수 없어서 이를 배제하였다.
- 처음엔 Expected Labeling Unit per Data가 칩 1개인 줄 알았는데, 바운딩 박스해야하는 개수 였다.
-  빛이 너무 강하거나 약해도 사람이 구분할 수 있다면(형체가 보인다면) bounding box를 한다.는 오묘한 표현이므로 이를 주변이 너무 하얗거나 너무 어두워서 edge가 흐려질 경우, bounding box하지 않는다로 바꾸는 것이 좋아보인다.

## 불량 검출 데이터 구축 시트(1번 구성용품 판별 모델)

| 주제                 | 내용                                                         |
|-----------------------|-------------------------------------------------------------|
| Data Type            | Image(jpg)                                                  |
| Data Amount          | 1200장(양품 600장, 불량품 600장), 배치 1 : 240장, 배치 2 : 960장                        |
| Expected Labeling Unit per Data | 0 ~ 9개                                               |
| Brief Description    | Bounding Box(바운딩 박스)|
| 종료 희망 날짜        | - 배치 1 : ~2025-1-24까지, - 배치 2 : ~ 2025-1-25까지       |
| Customer Guideline   | ![image](https://github.com/user-attachments/assets/b2c3a2d9-c467-41bf-bb62-80a08f8c1e6b) </br>보라색 : RASPBERRY PICO , 초록색 : HOLE, 하늘색 : BOOTSEL, 파란색 : OSCILLATOR, 빨간색 : USB, 노란색 : CHIPSET|
| Data Collection      | 자체 제작                                         |
| Annotation Type      | Bounding Box : 6종                                          |
| Class                | Bounding Box : 1. USB, 2. BOOTSEL, 3. CHIPSET , 4. OSCILLATOR,  5. RASPBERRY PICO, 6. HOLE|
| Property             | 정상 부분만 바운딩 박스한다.                                                        |
| Misc                 | 샘플이 컨베이어 벨트 밖, 혹은 카메라 범위를 벗어날 경우, 고장 부위를 판별할 수 없기 때문에 샘플은 반드시 카메라 범위 안에 들어와 있어야 한다. 또한, 카메라 범위 안에는 한 개의 샘플만이 있어야 한다. 왜냐하면 두 개의 샘플이 카메라 범위 안에 있을 경우, 둘 중 하나만 하자가 있어도 정상인 다른 샘플까지 모두 불량품으로 분류되기 때문이다. 구성용품을 바운딩 박스할 경우 엣지 기준으로 1픽셀 정도만 준다. 순서를 USB, BOOTSEL, CHIPSET, OSCILLATOR, HOLE, RASPBERRY PICO 순서로 바운딩 박스를 하여 서로 데이터를 검토할 때 무엇이 빠졌는지 확인할 수 있도록 한다.|
|Contact Info|이선우,김영수,한건희,최범석|

## 불량 검출 데이터 구축 시트(2번 불량 판별 모델)
| 주제                 | 내용                                                         |
|-----------------------|-------------------------------------------------------------|
| Data Type            | Image(jpg)                                                  |
| Data Amount          | 3720장(증강 2520장, 실제 1200장), 배치 1 : 증강 2520장, 배치 2 : 1200장                        |
| Expected Labeling Unit per Data | 1개                                               |
| Brief Description    | Bounding Box(바운딩 박스)|
| 종료 희망 날짜        | - 배치 1 : ~2025-1-29까지, - 배치 2 : ~ 2025-1-30까지       |
| Customer Guideline   | ![image](https://github.com/user-attachments/assets/02b95677-9996-467b-95b6-b79b9d65f31d) </br>파란색 : Broken , 빨간색 : Normal |
| Data Collection      | 자체 제작                                         |
| Annotation Type      | Bounding Box : 2종                                          |
| Class                | Bounding Box : 1. Broken, 2. Normal  |
| Property             | 칩(기판) 전체를 바운딩 박스한다.                                                        |
| Misc                 | 정상품 1개와 불량품 6개의 데이터를 360도 돌려서 사용했다. 왜냐하면 데이터가 적기 때문에 내부적으로 회전을 한 데이터를 이용해 학습한다.|
|Contact Info|이선우,김영수,한건희,최범석|

## FLASK UI
  - 컨테이너로 부터 온 이미지를 SuperbAI와 연결하여 웹에 이미지를 띄운다.
  - 구성용품 판별 모델과 불량 판별 모델, 원본 이미지를 웹에 띄워준다.
  - .env를 사용하여 올리기 민감한 정보를 관리하고 있다. 


    ACCESS_KEY=토큰 키 (superbAI 팀 키)</br>
    URL_1=예시 URL1 (첫번째 AI모델 URL)</br>
    URL_2=예시 URL2 (두번째 AI모델 URL)</br>


  - 사용법은 .env 파일을 생성하여
  -  환경설정을 한 후, app.py를 실행한다. 이때, 컨테이너에서 이미지를 보내는 HTTP와 superbai의 endpoint 2개가 필요하다.
## 전체 구조도

![image](https://github.com/user-attachments/assets/43a4595b-84c3-492a-9ed8-a6bafad19328)

  - 라즈베리를 통해 컨테이너, 카메라, 센서를 제어한다.
  - 플라스크를 통해 라즈베리로 부터 이미지를 HTTP를 통해 받는다.
  - 이 이미지를 superb AI의 endpoint에 보내 모델 결과를 통신 결과로 받는다.
  - 이 이미지를 웹을 통해 확인한다.
## 두 모델 선정 과정
### 구성용품 판별 모델
#### 개선 과정
  - 배치 1의 240장을 yolo 6 L-6, Deta를 돌려 성능을 확인, 성능이 바운딩 박스를 일부 못하거나, HOLE의 신뢰도가 낮은 것을 확인했다.
  - 이를 개선하기 위해 배치 2를 포함 1200개의 데이터를 학습시키고, 불량 판별 모델을 만들기로 한다. 왜냐하면 이는 모델, 데이터의 문제가 아닌 라벨링이 여러 구성용품으로 나뉘었기에 train Loss가 낮아지지 않는 현상을 발견했기 때문이다.
  - Deta 모델로 1200장을 학습하고, yolo로 불량 판별 모델을 학습하기로 결정하였다.
#### 모델 성능
  - 1200 모델의 경우 바운딩 박스를 올바르게 하긴 하지만, 부서진 구성용품을 바운딩 박스하거나 신뢰도가 60% 대가 나오는 HOLE 바운딩 박스가 있다.
#### 개선 방향
  - 실제 데이터 셋을 기반으로 데이터를 수집하여 학습시킨다. 이는 240 -> 1200장의 학습량 증가에 따른 성능이 올라갔기 때문이다.
  - 학습이 잘 안되는 class의 임베딩 분포와 현재 학습하는 데이터의 분포를 보고 어떠한 방식으로 학습해 나아갈지 정한다.
### 불량 판별 모델
#### 개선 과정
  - 증강 데이터 2520개 만 돌릴 경우, yolo6 N의 모델이 실제 데이터 셋에 대해서 성능이 좋지 않았다. 그러므로 실제 데이터를 추가하여 학습하였다. 하지만 이 경우, Normal로만 바운딩 박스를 하거나 Broken으로만 바운딩 박스를 하는 편향 문제가 두드러졌다. 이를 해결하기 위해 `정상품 : 불량품` 비율을 바꿔가면서 비교했으나 여전히 편향 문제가 있었다. 데이터 셋을 분석하니 특정 방향의 데이터가 Normal class에 분포해있다는 것을 발견하였다.
#### 모델 성능
  - Normal, Broken에 편향되어 결과가 나온다.
#### 개선 방향
  - 다양한 방향의 실제 데이터를 넣어 학습한다. 증강 데이터의 경우, 내부 yolo6 N에도 있지만, 데이터 수를 채우기 위해 사용했었다. 하지만 실제 데이터와 사용할 경우, 실험을 많이 하지 않아서 알기 어렵지만 일부 도움이 되지만 실제 데이터에 비해 성능 향상에 떨어지는 것으로 보인다. 왜냐하면 실제 데이터로 했을 경우, 바운딩 박스를 안하는 경우가 적지만, 증강 데이터를 섞을 경우, 바운딩 박스를 안하는 경우가 늘었다. 이를 해결하기 위해 증강 데이터로 모델을 학습한 후에, 실제 데이터를 학습하는 방법을 쓴다면 성능 향상이 있을 것이다. 또한 정상품과 불량품 비율을 조절하여 어느 한쪽에 오버피팅이 안되도록 한다.
  - 앞선 모델 개선 방법처럼 데이터 셋을 분석하고 어떠한 문제가 있는지 토론하여 이를 개선한다.
## 데모영상
  - 팀원들에게 유튜브 링크로 볼 수 있게 만듦
## 프로젝트 후기

