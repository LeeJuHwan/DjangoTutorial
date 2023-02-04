### STEP 14

- TEMPLATE & MODEL 
    - COMBINE
        - 테이블 데이터를 쿼리를 이용하여 조회 한 후 템플릿의 context로 넘겨주는 단계

- code
    `polls/templates/polls/index.html`
    ```
    {% extends 'base.html' %}
    {% block content %}
        {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
            <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
        {% endfor %}
        </ul>
        {% else %}
        <p>No polls are available.</p>
        {% endif %}
    {% endblock content %}
    ```
    - HTML 태그는 베이스 파일에서 상속 받는다.
    - 진자 템플릿의 조건과 반복문을 이용하여 자료가 있을 때와 없을 때의 방식으로 처리한다.
    - 리다이렉션 구문을 urlpattern의 name들을 가지고 하는 방법과, 직접적으로 url을 주는 방법으로 실행했다.

    <img width="410" alt="image" src="https://user-images.githubusercontent.com/118493627/216776086-8a46d0eb-a585-4913-b4d4-72ac97f1db71.png">

    `polls/views.py`
    ```
    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        context = {"latest_question_list" : latest_question_list}
        return render(request, "polls/index.html", context)
    ```
    - latest_question_list로 쿼리를 통해 return된 값을 저장한다.
    - context를 딕셔너리 형태로 값을 저장하여 template을 통해 값을 전달한다.