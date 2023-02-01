### STEP 6

- TEMPLATES
    - syntax : Jinja2
    - web programing에 기본이 되는 구조를 로드 할 수 있다.

    - render(requets, template_name, context = None)
        - context : template안으로 데이터를 넘길 수 있고, 이 데이터는 html 과 합쳐지게된다.
    - Steps
        - `settings.py`에 INSTALL_APPS 를 변경하면 된다.
        - `templates` 라는 디렉터리 생성
        - django.shortcuts 모듈 안에 render를 import
    <img width="2084" alt="image" src="https://user-images.githubusercontent.com/118493627/215969729-1daac8cd-3252-4ab6-b9b3-4d2265c18252.png">

    - Templates tructure
        1. templates in root
            - DJANGO_ROOT/templates/<APP_NAME>/<TEMPLATES_FILE>
            - 프로젝트 규모가 커질 경우에 devops가 CDN으로 옮기기 좋다.

        2. templates under the app
            - <APP_NAME>/templates/<APP_NAME>/<TEMPLATES_FILE>
            - 패킹 하기 쉽다.
            - 다른 프로젝트에 패키지를 재사용 할 수 있다.

            <img width="699" alt="image" src="https://user-images.githubusercontent.com/118493627/215970833-5d4b3493-ad56-498f-ba8e-d6b606109c0e.png">

- code
    - `mysite/setting.py` [ADD]
        ```
        INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "polls.apps.PollsConfig"
        ]
        ```
    - `polls/views.py`
        ```
        def index(request):
            return render(request, "polls/main.html")
        ```

    - `polls/templates/polls/main.html`
    ```
    <html>
        <body>
            <h1> hello world </h1>
        </body>
    </html>
    ```
<img width="481" alt="image" src="https://user-images.githubusercontent.com/118493627/215972549-61150032-8b04-467b-b651-1f3cd395c6f5.png">