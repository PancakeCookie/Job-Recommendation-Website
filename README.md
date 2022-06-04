# 취하자 - 직업추천웹사이트


한국고용정보원 재직자 설문조사 데이터 기반으로 제작된 웹사이트 입니다.  
https://github.com/PancakeCookie/DACON-Job-Recommendation-Competition

## 기술 스택
Front-end : bootstrap  
Back-end : django  
DB : MySQL  
배포 : AWS EC2, S3, RDS  

## 기능 
- 회원가입, 로그인, 로그아웃
- 직업 통계, 고용지표  
- 직업 추천 설문 
- 직업 정보(워크넷 연동)
- 추천 직업 기반 일자리 정보 제공

### 메인 페이지
<img src = "images/front.png" >
<img src = "images/eda.png" >

### 추천 직업 기반 일자리 정보 제공
<img src = "images/jobapi.png" >
서울시 일자리 포탈 api 이용

### 직업 추천 설문 
<img src = "images/rec.png" >


### 직업 추천 결과 

<img src = "images/result.png" > 
상위3개 직업 추천시 ACCURACY ~% 

기존의 약 600개의 직업 중 중분류 ~개로 분류 및 통합
4개년도 질문을 통합-질문 500개 중에 FEATURE IMPORTANCE 가 높은 질문들 중 70개를 간추려 제작




