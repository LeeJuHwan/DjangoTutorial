### STEP 10

- STATIC FILES

    - Settings
        - INSTALLED_APPS
            - 'django.contrib.staticfiles
        - STATIC URL
        - static 폴더 만들기

    - STATIC_URL
        - Static file 저장하는 곳

    - STATIC_ROOT
        - static collect하는 명령어가 있는 곳
        - 모든 static 파일을 한 곳에 모아서 새로운 디렉터리로 옮겨주는 것

    - STATIC_ROOT
        - 여러군데 분산 되어 있는 것을 한 곳으로 뭉쳐주는 것

    - STASTICFILES_DIRS
        - static 폴더 말고도 다른 곳에 static 파일이 있다면 읽을 수 있도록 도움을 주는 것

    - MEDIA_ROOT
        - Django app 안에 파일을 업로드 할 때 저장되는 곳


- code
    - settings
        - DEBUG = True
        ```
        STATIC_ROOT = ""
        STATIC_URL = "/static/"
        STATICFILES_DIRS = ("static", )
        ```

    - `main.html`
        ```
        {% extends "base.html" %}
        {% load static %}

        {% block content %}
            <img src="{% static 'mysite/다운로드.jpeg' %}" alt="Bear image" />
        {% endblock content %}
        ```

    
