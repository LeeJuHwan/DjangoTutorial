### STEP 8

- TENMPLATS URL

- TEMPLATES INHERITANCE
    - block
        - 나중을 위해 사용 할 빈 공간
    - extends 
        - 두번째 페이지에서 해당 페이지를 읽는 행위

    <img width="2015" alt="image" src="https://user-images.githubusercontent.com/118493627/216035337-da648b24-21b0-46d1-965b-2155bd76e235.png">

- code
    - `settings.py`
        ```
        TEMPLATES = [
        {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")], # 수정할 곳
        "APP_DIRS": True,
        ```

    - `base.html`
        ```
        <body>
            {% block content %}
            {% endblock %}
        </body>
        ```
        
    - `main.html`
        ```
        {% extends 'base.html' %}
        {% block content %}
            <h1> 
                <a href="{% url 'polls:detail' question_id=10 %}">Question 10</a>
            </h1>
            <h1>{{ greetings|lower }}</h1>
            <h2>I am from {{ location.city }}, {{ location.country }}</h2>
            <h2>I speaks {{ languages.0 }} and {{ languages.1 }}</h2>
            <ul>
                {% for lang in languages %}
                    <li>{{ lang }}</li>
                {% endfor %}
                
                {% for lang in languages %}
                    <li>
                        {% if lang == "Korean" %}
                        condition Korean!
                        {% else %}
                        condition English!
                        {% endif %}
                    </li>
                {% endfor %}
            </ul>

            <ul>
                {% for k, v in location.items %}
                    <li>{{ k|capfirst }}: {{ v|capfirst }}</li>
                {% endfor %}
            </ul>
        {% endblock %}
        ```

    - 폴더 구조
    <img width="300" alt="image" src="https://user-images.githubusercontent.com/118493627/216043688-04f87dab-30f6-47f4-bc9c-83efb67081c1.png">