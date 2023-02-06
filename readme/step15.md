### STEP 15

### ADMIN PAGE
    - 장고 프레임워크의 가장 강력한 기술 중 하나이다.
    - 모델에 대한 meta data를 읽을 수 있고, page access의 접근 권한을 설정할 수 있다.
<img width="1080" alt="image" src="https://user-images.githubusercontent.com/118493627/216869796-c5ee61b0-d7c3-4e72-b9a2-108ef0ecebe5.png">

- 슈퍼유저 명령어를 통해서 유저를 생성하고 페이지를 접속하면 생성된 유저만 접근이 가능하다.

    <img width="1052" alt="image" src="https://user-images.githubusercontent.com/118493627/216870068-4000f2bf-7bce-48a0-b62c-da083d424caa.png">

- 생성된 앱 관리 기능
<img width="1064" alt="image" src="https://user-images.githubusercontent.com/118493627/216870302-ca5febcf-0cb2-4eb1-98a9-9f5c53cba5b8.png">

- Code
    - createsuperuser & runserver
        ```
        python manage.py createsuperuser

        python manage.py runserver
        ```
        - 비밀번호는 8글자 이상으로 해야 하고, 이메일 또는 계정의 이름과 비슷한 경우로 설정할 수 없었다.

        <img width="652" alt="image" src="https://user-images.githubusercontent.com/118493627/216870984-64272f97-a40c-40fb-a119-97209ce710b7.png">

        - connect admin page
            - http://127.0.0.1:8000/admin/login/?next=/admin/

        <img width="648" alt="image" src="https://user-images.githubusercontent.com/118493627/216870757-200c45b8-ce16-4d65-9614-a2751ab5b556.png">

        <img width="1305" alt="image" src="https://user-images.githubusercontent.com/118493627/216871237-3728ebb1-3179-4fe4-bb33-5219299bf6b8.png">

    - 사용중인 app을 admin과 연동
        ```
        from django.contrib import admin
        from .models import Question

        admin.site.register(Question)
        ```
        <img width="1284" alt="image" src="https://user-images.githubusercontent.com/118493627/216872382-ac0513c6-6fb1-4621-9f36-381e11a47dcb.png">

    - 연동 된 app의 데이터베이스에 접근하여 CRUD 권한 이용
        - validation이 걸려있기 때문에 owner의 글자 길이를 맞춰줘야 하는데 너무 대충 적어서 에러가 난 모습이다. 

        <img width="953" alt="image" src="https://user-images.githubusercontent.com/118493627/216871732-68623fc8-d70a-4c8a-bed5-0f40ac52d3a1.png">

        - 기존 데이터베이스에 추가 된 것을 확인할 수 있다.

        <img width="943" alt="image" src="https://user-images.githubusercontent.com/118493627/216871978-5eb49247-c989-4cf0-a788-c1a572673b78.png">

        - 디테일 화면으로 들어가서 삭제하는 기능도 지원 하고 있지만, 여러개를 선택하여 지원하는 것도 가능하기 때문에 사용자가 접근하기 쉬운 GUI 환경을 서포트하는 프레임워크로 다루기가 매우 편한 것 같다.
