# STEP 4

## Authentication
<img width="912" alt="image" src="https://user-images.githubusercontent.com/118493627/223640568-3e149bd3-a8b3-446c-826e-b252d99436b3.png">

- 유저의 개인화 시스템 중 로그인, 로그아웃 등의 기능을 뜻한다.

- Django contrib auth urls를 상속 받으면 path를 별도로 login, logout, password chage 등 추가를 하지 않아도 내부에서 라우팅 할 수 있게 지원한다.

<img width="1113" alt="image" src="https://user-images.githubusercontent.com/118493627/223641110-70056cd4-c3be-48d4-990c-a1e3661395d8.png">

- project root - template 생성 - registry 폴더 생성 - login.html 을 갖은 구조로 폴더를 생성

- `settings.py`에서 DIRS 설정
    - root 폴더에 있는 templates를 사용하기 위해 셋업

- Login_redriect_url = 로그인 후 어디로 리다이렉트 할 것인지 지정

- 로그인 후
    - 유저가 템플릿에 렌더링 했을 때 is_athenticated 메소드를 이용 해서 정상 로그인인지 인증을 할 수 있다.
    -  get_username 메소드를 이용해서 로그인 한 유저의 이름을 호출 할 수 있다.
- 로그아웃
    - logged_out.html 을 템플릿 안에 생성

<img width="1044" alt="image" src="https://user-images.githubusercontent.com/118493627/223642447-2ef5853c-b06b-4bb3-9355-876c4ebff485.png">

- 로그인을 하지 않았을 경우 내부 페이지를 보여주지 않게끔 유도할 수 있다. -> FBVs, CBVs를 사용 할 수 있는데 서로 사용 방법이 틀리다.
    - FBVs
        `@login_required` 라는 데코레이터를 호출 하여 정상 로그인 한 유저인지 인증 할 수 있다.
    - CBVs
        `LoginRequiredMixin`이라는 클래스를 상속 받아서 유저 인증을 진행할 수 있다.

- ABOUT CODE
    - [공식 문서](https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.views.LoginView)

    - `dealershop/urls.py`
        ```
        path('accounts/', include('django.contrib.auth.urls')),
        ```

    - login & logout
        - `dealershop/templates/registration/login.html`
            ```
            {% comment %} https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.views.LoginView {% endcomment %}
            {% if form.errors %}
            <p>Your username and password didn't match. Please try again.</p>
            {% endif %}

            {% if next %}
                {% if user.is_authenticated %}
                <p>Your account doesn't have access to this page. To proceed,
                please login with an account that has access.</p>
                {% else %}
                <p>Please login to see this page.</p>
                {% endif %}
            {% endif %}

            <form method="post" action="{% url 'login' %}">
            {% csrf_token %}
            <table>
            <tr>
                <td>{{ form.username.label_tag }}</td>
                <td>{{ form.username }}</td>
            </tr>
            <tr>
                <td>{{ form.password.label_tag }}</td>
                <td>{{ form.password }}</td>
            </tr>
            </table>

            <input type="submit" value="login">
            <input type="hidden" name="next" value="{{ next }}">
            </form>

            {# Assumes you set up the password_reset view in your URLconf #}
            <p><a href="{% url 'password_reset' %}">Lost password?</a></p>
            ```
        - `dealershop/templates/registration/logged_out.html`
            ```
            <div>
                <p>You are not authenticated</p>
                <p>Please login by clicking <a href="{% url 'login' %}">here</a></p>
            </div>
            ```
    - `inventory/templates/inventory/main.html`
        ```
        <h1>main index page welcome {{ name }} is success logged in </h1>
        {% if user.is_authenticated %}
            <p>You are logged in as  {{ user.get_username }}</p>
            <p><a href="{% url 'logout' %}?next={{request.path}}">Log out</a></p>
        {% else %}
            You are not logged in yet! Please login by clicking <a href="{% url 'login' %}?next={{request.path}}">here</a>
        {% endif %}
        ```
---

## SIGN-UP
 <img width="1008" alt="image" src="https://user-images.githubusercontent.com/118493627/223749553-d0f01649-63ca-44f5-8692-5c74f3896a8e.png">

- built-in form
    - 만약, 내재 되어 있는 view 기능을 원치 않는다면 메뉴얼로 폼을 사용 하고 싶진 않고, Authentication을 사용 하고 싶다면 `django.contrib.auth.form`을 사용해서 만들 수 있다.

<img width="980" alt="image" src="https://user-images.githubusercontent.com/118493627/223752236-3a6c9445-45c1-4fd1-9b71-f42e00a14d44.png">

---

## DJANGO-ALLAUTH
<img width="1157" alt="image" src="https://user-images.githubusercontent.com/118493627/224057744-1bf462de-299b-454b-96fe-2cfc6c1e3860.png">

- [공식 홈페이지](https://django-allauth.readthedocs.io/en/latest/)
- 로그인, 로그아웃, 회원가입, 소셜 로그인 지원

- 설치
    ```
    pip install django-allauth
    ```
### ABOUT CODE
- setting
    - `dealershop/settings.py`
        - template
            ```
            "django.template.context_processors.request",
            ```
        - authentication backend
            ```
            AUTHENTICATION_BACKENDS = [
            'django.contrib.auth.backends.ModelBackend',

            'allauth.account.auth_backends.AuthenticationBackend'],
            ```
        - installed apps
            ```
            'django.contrib.sites',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            ```
        - site id
            ```
            SITE_ID = 1
            ```
- url
    - `dealershop/urls.py`
        ```
        path("accounts/", include("allauth.urls")),
        ```

- tempalte
    - `inventory/temapltes/inventory/main.html`
        ```
        {{ logout }} -> {{ account_logout }}

        {{ login }} -> {{a ccount_login }}
        ```

- migrate
    ```
    python manage.py migrate
    ```

### allauth customizing
- [공식 깃허브](https://github.com/pennersr/django-allauth/tree/master/allauth/templates/account)

<img width="726" alt="image" src="https://user-images.githubusercontent.com/118493627/224064998-27fe1aa2-7e3b-41ca-aed3-6ae9478eab2b.png">

- 깃 허브에 있는 템플릿을 동일 폴더 구조로 구성한 뒤, 내용 변경 및 CSS 추가 