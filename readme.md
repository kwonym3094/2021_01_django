# Django(장고) 프로젝트 생성
## 1.가상환경 만들기
    - cd <project dir>
    - python -m venv .venv
    - cf) git에 가상환경을 올릴 필요는 없으므로 echo '.venv' >> .gitignore
## 2. 가상환경 활성화
    - cd .venv/Scripts
    - activate or activate.bat (비활성화는 deactivate)
    - cf) 일일이 폴더에 들어가서 가상환경을 활성화 해주는 것은 번거로우므로 배치파일 생성하여 바로 실행하는 것을 권장
        * 경로에 맞게 다음 예제와 같이 작성하여 .cmd 파일 만들기
          @echo off
          D:
          cd D:Project/2021_01_django
          D:/Project/2021_01_django/.venv/Scripts/activate
        * win+R -> sysdm.cpl -> 고급 -> 환경변수 -> 사용자변수 path 편집 -> cmd파일이 있는 경로 새로만들고 저장
        * cmd에서 확인 ex) D:\Project>django_exec
## 3. Django 프로젝트 생성
    - django 패키지 다운: pip install django (가상환경이 활성화 되어있는 상태에서만 !!)
    - pip 가 최신버전이 아니라고 하면 python -m pip install --upgrade pip 입력하여 pip 최신버전으로 업데이트
    - django-admin startproject config . << config: config라는 프로젝트를 장고 내에 생성, . : 현재 디렉토리에 어플리케이션 생성
## 4. Django 프로젝트 내용물 확인
        C:\projects\mysite
        ├── config/
        │      ├─ asgi.py : wsgi와 같은 기능을 하는 것으로 예상됨
        │      ├─ settings.py : Django 내 설정들을 모아놓는 파일
        │      ├─ urls.py : 프로젝트에 접근하기 위한 첫번째 문지기. 어떠한 요청이 django 서버에 오면, 그 요청이 도착하는 곳. 요청 분석해서 다른 곳으로 전환하는 중계기(라우터) 역할
        │      ├─ wsgi.py : 실제로 서비스를 하기 위해서, 완성을 해서 24시간 돌아가는 서버에다가 코드를 올려놓고 사람들이 access하고 수정할 수 있게 하는 파일
        │      └─ __init__.py : config라는 폴더를 하나의 패키지/모듈로 인식시킴. 이를 통해 config.urls, config.settings와 같은 기능 사용가능. 파이썬파일 불러오기 위해 __init__파일 필요
        └── manage.py
## 5. Django 프로젝트 실행
    - python manage.py runserver ($IP:$PORT)

## 번외
    - 현재 사용한 패키지 구성 그대로 다른 프로젝트에서 사용하고 싶을 때?
        * pip freeze > requirements.txt << 현재 설치된 패키지 목록을 requirements.txt라는 파일에 저장
        * requirements.txt라는 파일만 나중에 다른 프로젝트로 이동시켜 pip install -r requirements.txt 해주면 됨
        * 혹시 충돌날 경우를 대비해 해당하는 패키지만 다 지우는 경우? >> pip uninstall -r requirements.txt -y