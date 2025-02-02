
## 첫번째 프로젝트
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

## 불량 검출 데이터 구축 시트

| 주제                 | 내용                                                         |
|-----------------------|-------------------------------------------------------------|
| Data Type            | Image(jpg)                                                  |
| Data Amount          | 1200장(양품 600장, 불량품 600장), 배치 1 : 240장, 배치 2 : 960장                        |
| Expected Labeling Unit per Data | 0 ~ 4개                                               |
| Brief Description    | Image Category(분류) / Bounding Box(바운딩 박스)을 통한 양품, 불량품 판별 |
| 종료 희망 날짜        | - 배치 1 : ~2025-1-24까지, - 배치 2 : ~ 2025-1-25까지       |
| Customer Guideline   | 더미 |
| Data Collection      | 자체 제작                                         |
| Annotation Type      | Image Category : 2종, Bounding Box : 4종                                          |
| Class                | Image Category : 1. Good product 2. Faulty product,  Bounding Box : 1. USB 2. BOOTSEL, 3. CHIPSET , 4. OSCILLATOR|
| Property             | 없음                                                        |
| Misc                 | 샘플이 컨테이너에 바깥에 걸쳐져 있어도, 데이터로 사용한다. 칩이 사진에 짤리거나 컨테이너 바깥쪽에 걸쳤을 때, 불량품이 짤릴 경우, 불량품의 50프로 이상이면 바운딩 박스를 한다. 주변의 채광을 가림막을 이용하여 밝기를 일정하게 조절한다. 바운딩 박스의 경우, 예시 사진을 몇 개 넣어 불량품의 3~7 픽셀의 패딩을 넣어서 바운딩 박스를 설정한다.|
|Contact Info|이선우,김영수,한건희,최범석|

## FLASK UI
  .env를 사용하여 올리기 민감한 정보를 관리하고 있다. 

  ACCESS_KEY=ywmBNfb6TQ7gBJNzAVVolazNLa2pDcXT9qgluUch(superbAI 팀 키키)
  URL_1=https://suite-endpoint-api-apne2.superb-ai.com/endpoints/1c49f6a4-15e9-4631-a48e-9df69decddd4/inference(첫번째 AI모델 URL)
  URL_2=https://suite-endpoint-api-apne2.superb-ai.com/endpoints/27b67988-30b5-4205-be8e-4224b27dd992/inference(두두번째 AI모델 URL)