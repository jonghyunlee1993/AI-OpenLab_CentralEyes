---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
marp: true
---

# Vision Lab - 가운데 눈
### 중간 발표

김창곤, 김태윤, 오민영, 이종현, 이휘준

---

# Table of Contents

1. 스터디 진행 사항
$~~~~~~~~~~~~$
2. 프로젝트
$~~~~~~~~~~~~$
3. 향후 일정
$~~~~~~~~~~~~$
4. 각자 회고

---
# 1. 스터디 진행 사항

1. 모임 시간: 매주 토요일 20:30 ~ 24:00
$~~~~~~~~~~~~$
2. 핵심 가치: 논문 리딩, 적용 가능한 실습
$~~~~~~~~~~~~$
3. 프로젝트 : 논문과 실습을 아우르는 '우리만의' 프로젝트

---
# 1. 스터디 진행 사항

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

![width:800 height:520 center](./time_table.png)

---
# 1. 스터디 진행 사항: 이론

1. object detection 경향 파악
    - DL 기반의 object detection 경향을 정리한 리뷰 페이퍼  
2. 2 stage 계열 object detection 
    - RCNN, fast RCNN, faster RCNN, mask RCNN
3. 1 stage 계열 object detection
    - YOLO v1, v2, v3, SSD, RetinaNet
4. various computer vision 리뷰
    - ResNet, Sort & DeepSort, Conv weigh visualization

---
# 1. 스터디 진행 사항: 실습

1. 개발 환경 세팅
    - docker
    - git & git hub
2. DL framework: Keras
    - data loader
    - image data augmentation
    - pre-trained model fine tuning
    - model ensemble and hard voting

---
# 1. 스터디 진행 사항:실습

3. image data annotation tool
    - CVAT
    ![width:600 height:280](./data_annotation.png)
4. CNN based image classification, regression
    - 인공지능 경진대회 예선, 본선 대회 참가

---
# 1. 스터디 진행 사항: 실습

5. AutoML
    - pycaret 라이브러리
    - https://dacon.io/competitions/official/235647/codeshare/1701?page=1&dtype=recent&ptype=pub 

---
# 2. 프로젝트

축구 중계 영상에서 선수, 축구공 Object Detection (+ Tracking) 하기

![width:800 height:450 center](./project_example.png)

---
# 2. 프로젝트: dataset

1. Fitogether 제공 데이터셋
    - 2019, 2020 시즌 K리그 경기장에서 획득한 고정 카메라 영상
    - 4K 25fps 영상, 4479 프레임 (약 3.5분)
    - Players, Ball, Others / 3개의 레이블

---
# 2. 프로젝트: dataset

![width:800 height:500 center](./fitogether_dataset_sample.png)

---
# 2. 프로젝트: dataset

2. 스터디 생성 데이터셋
    - youtube 영상을 youtube-dl 프로그램을 이용하여 다운로드
        - 중계 영상 및 하이라이트 영상
    - 매 100 프레임마다 1개 프레임 추출
    - CVAT 툴을 이용하여 해당 영상 레이블링
    - Players, Ball / 2개의 레이블
    - 학습용: 100 프레임, 검증용: 100 프레임
---
# 2. 프로젝트: dataset

![width:800 height:500 center](./study_dataset_sample.png)

---
# 2. 프로젝트: preprocessing

영상 해상도가 제각각 -> bounding box를 중심으로 하는 작은 이미지로 crop & bounding box의 좌표 수정

![width:380 height:380 center](./boxwise_crop_image_sample.png)

---
# 2. 프로젝트: preprocessing

전처리 이후 데이터셋
1. Fitogether 제공 데이터 셋
    - 10554 장
2. 스터디 생성 데이터 셋
    - 951 장

---
# 2. 프로젝트: model

1. YOLO v3 (pytorch version)
    - https://github.com/ultralytics/yolov3

2. YOLO v5 (pytorch version)
    - https://github.com/ultralytics/yolov5

</br>
추후 도전 과제

- 2 stage 계열 모델 (RCNN 계열)

---
# 2. 프로젝트: model

1. 이미지를 그리드로 분할
2. 각 그리드를 중심으로 하는 박스를 중심으로 탐색
3. 박스 안에 오브젝트가 있나? 있다면 어떤 오브젝트인가?

---
# 2. 프로젝트: model

![width:500 height:500 center](./yolo_model_description.png)

--- 
# 2. 프로젝트: model

- 실시간 (1초당 20 frame 이상) 처리가 가능하고 준수한 정확도
- CCTV, 로봇, 자율 주행 등에 널리 쓰이고 있음

![width:500 height:350 center](./yolo_model_example.png)

---
# 2. 프로젝트: fine tuning results
</br>
</br>


---
# 2. 프로젝트: prediction sample



---
# 3. 향후 일정

![width:700 height:500 center](./아직한발남았다.png)

---
# 3. 향후 일정

약 2주 간의 Tracking 모듈 구현을 위한 여정이 남아있습니다.
(우리 팀원들 모두 동의한 것 맞죠?)

Sort 및 Deep Sort 알고리즘
- https://github.com/theAIGuysCode/yolov3_deepsort
- https://github.com/LeonLok/Deep-SORT-YOLOv4

등을 참고하여 진행할 계획

---
# Q&A
</br>
</br>
</br>
</br>

## $~~~~~~~~~~~~~~~~~~~~~~~~~$ Thank you! 