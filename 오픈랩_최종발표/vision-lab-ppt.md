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

김창곤, 김태윤, 오민영, 이종현

---

# Table of Contents

1. 기존 목표
$~~~~~~~~~~~~$
2. 진행 사항
$~~~~~~~~~~~~$
3. 향후 목표
$~~~~~~~~~~~~$
4. 프로젝트 소개

---
# 1. 기존 목표

1. 모임 시간: 매주 토요일 20:30 ~ 24:00
$~~~~~~~~~~~~$
2. 핵심 가치: 논문 리딩, 적용 가능한 실습
$~~~~~~~~~~~~$
3. 프로젝트 : 논문과 실습을 아우르는 '우리만의' 프로젝트

---
# 1. 기존 목표

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

![width:800 height:520 center](./time_table_before.png)

---
# 2. 진행 사항: 이론

1. object detection 경향 파악
    - DL 기반의 object detection 경향을 정리한 리뷰 페이퍼  
2. 2 stage 계열 object detection 
    - RCNN, fast RCNN, faster RCNN
3. 1 stage 계열 object detection
    - YOLO v1, v2, v3, SSD
4. various computer vision 리뷰
    - ResNet, RetianNet, DeepSort 알고리즘, convolutional layer 시각화

---
# 2. 진행 사항

![width:1000 height:600 center](./time_table_after.png)
---
# 2. 진행 사항: 실습

1. 개발 환경 세팅
    - docker
    - git & git hub  
2. DL framework: Keras
    - data loader
    - image data augmentation
    - pre-trained model fine tuning
    - model ensemble and hard voting

---
# 2. 진행 사항: 실습

3. image data annotation tool
    - CVAT
    ![width:600 height:280](./data_annotation.png)
4. CNN based image classification, regression
    - 인공지능 경진대회 예선, 본선 대회 참가
---

# 3. 향후 목표

1. 우리만의 데이터셋을 가지고 Object Detection + Tracking 해보자
    - Data annotation tool을 이용해서 직접 데이터를 만들고 학습시켜보자
    - YOLO, DeepSort 등 가장 활발하게 사용되는 open source를 이용해보자
$~~~~~~~~~~~~$
2. 나만의 CNN 코드 템플릿을 만들자
    - pre-trained model fine tuning, image data augmetation 등이 구현되어 있는 나만의 템플릿 만들어서 이미지 대회에 적용해보자


---

# 4. 프로젝트 소개

축구 중계 영상에서 선수, 축구공 Object Detection + Tracking 하기

![width:800 height:450 center](./project_example.png)

---

# Q&A
</br>
</br>
</br>
</br>

## $~~~~~~~~~~~~~~~~~~~~~~~~~$ Thank you! 