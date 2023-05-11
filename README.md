# Project : Image caption generator

![demo](https://user-images.githubusercontent.com/119550025/235557691-6e3e6add-8f13-4936-a13c-b8801e8cbf92.png)

--------------------

### Image Captioning 은 NIC(Neural Image Captioning)이라고도 하며, 이미지를 입력으로 받아들여, 해당 이미지에 대한 설명을 자연어로 생성하는 기술입니다. 

### 즉, 이미지와 관련된 텍스트 설명을 자동으로 생성하는 것입니다. 이를 통해 이미지의 시각적인 정보를 더욱 풍부하게 전달할 수 있습니다.



### 현재 프로젝트에선 모델에의해 생성된 자연어결과값과 한국어번역, 텍스트를 오디오로 변환하여 제공하고 있습니다.

-----------------------------



### 해당 모델은 Soft attention 을 활용하여 CNN 엔코더 + LSTM 디코더로 이루어져 있습니다.

![KakaoTalk_20230511_205549155](https://github.com/devseungil/Image-caption-project/assets/119550025/71f6cd93-5586-4550-a378-463f5561fa07)

----------------------------------

### Service 탭에서 이미지 파일을 업로드하며 생성된 모델을 확인해보세요.

------------------

Home : 이미지 캡션과 모델구현방법에 대한 설명

Service : 실제 이미지 입력창

Project ideas : 추후 구현할 UI와 기능목록

About us : 프로젝트 팀과 팀원에대한 정보

--------------------------

### 실행방법

플라스크 가상환경설정

- pip install virtualenv (가상환경 라이브러리 설치)

- virtualenv 가상환경명 (가상환경명 으로 가상환경 생성)

가상환경 활성화

- source 가상환경명/Scripts/activate
- pip install -r requirement.txt

가상환경 실행 후 터미널에 python app.py 입력 로컬서버도메인 Ctrl + 클릭

Ctrl + c 2번입력 하면 서버 종료





