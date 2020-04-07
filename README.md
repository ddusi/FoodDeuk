## Fooddeuk

1. 설치해야할 라이브러리

   - python django
   - python pymysql
   - python mysql client

2. django 실행 명령어

   ```
    python manage.py runserver
   ```

3. 접속 URL

   ```
    127.0.0.1:8000/main
   ```

   URL은 기본적으로 2개로 갈라짐.

   ```
    /main
    			/singup
    			/singin
    /swipe 
    			/mypage
    			/detail/<int:id>
    			/like
    			/about
   ```