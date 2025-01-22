
## 첫번째 프로젝트
  - 칩의 구성용품 라벨링 프로젝트

| 주제                 | 내용                                                         |
|-----------------------|-------------------------------------------------------------|
| Data Type            | Image(jpg)                                                  |
| Data Amount          | 132장, 배치 1 : 66 장, 배치 2 : 66장                        |
| Expected Labeling Unit per Data | 0 ~ 9개                                              |
| Brief Description    | 주어진 이미지에서 객체를 bounding box 하는것 - 칩의 구성요소를 파악하는 bounding box 진행하기 |
| 종료 희망 날짜        | - 배치 1 : ~2025-1-22까지, - 배치 2 : ~ 2025-1-22까지       |
| Customer Guideline   | ![Screenshot from 2025-01-22 14-28-14](https://github.com/user-attachments/assets/1e5a0b7c-62d5-4dc1-bd51-251a0c3bae7d) 빨간색 : RASPBERRY PICO , 주황색 : HOLE, 노란색 : BOOTSEL, 연두색 : OSCILLATOR, 파란색 : USB, 보라색 : CHIPSET|
| Data Collection      | 강사님 제공 데이터                                           |
| Annotation Type      | Bounding Box : 6종                                          |
| Class                | 1. RASPBERRY PICO, 2. HOLE, 3. BOOTSEL, 4. OSCILLATOR, 5. USB, 6. CHIPSET |
| Property             | 없음                                                        |
| Misc                 | 칩이 사진에 짤리거나 컨테이너 바깥쪽에 걸쳐서 구성용품이 짤릴 경우 구성용품의 50프로 이상이 보일 경우, 바운딩 박스를 한다. 빛이 너무 강하거나 약해도 사람이 구분할 수 있다면(형체가 보인다면) bounding box를 한다.|
|Contact Info|이선우,김영수,한건희,최범석|

- 특이사항 : 부품 고장을 라벨링 안하는 이유는 데이터셋에 고장이 났다는 표시나 이미지를 확인할 수 없어서 이를 배제하였다.
- 처음엔 Expected Labeling Unit per Data가 칩 1개인 줄 알았는데, 바운딩 박스해야하는 개수 였다.
-  빛이 너무 강하거나 약해도 사람이 구분할 수 있다면(형체가 보인다면) bounding box를 한다.는 오묘한 표현이므로 이를 주변이 너무 하얗거나 너무 어두워서 edge가 흐려질 경우, bounding box하지 않는다로 바꾸는 것이 좋아보인다.
|class                      |Annotation type          |부가설명                    |
|--------------------------|--------------------------|--------------------------|
|RASPBERRY PICO|Box|전체 칩 모형|
|HOLE          |Box|칩을 고정할 수 있는 4개의 핀|
|BOOTSEL        |Box|부트시 필요한 데이터를 저장하는 메로리|
|OSCILLATOR      |Box|주기 신호를 생성하는 칩|
|USB            |Box|USB를 연결할 수 있는 단자|
|CHIPSET        |Box|주요 구성 요소들 간의 데이터 흐름을 관리하는 칩셋이다|
