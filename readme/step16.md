### STEP 16

### FORM
- 유저에게 input을 받은 값을 서버 사이드로 처리하는 방법

### HTTP REQUEST METHODS
- 여러가지 http request의 방법을 알아보자

<img width="1006" alt="image" src="https://user-images.githubusercontent.com/118493627/216873029-477e68b8-1bc8-41bd-8a11-960ae09dc2a2.png">

- 중요한 methods
    - GET : 리소스 정보를 조회할 때
    - POST : 유저의 information을 서버로 전달 할 때 
    - PUT : 데이터를 변경하고 싶을 때
    - DELETE : 리소스를 삭제하고 싶을 때

    <img width="1025" alt="image" src="https://user-images.githubusercontent.com/118493627/216873697-9a50b21a-d1d2-4de8-9146-51b7de2fe9d4.png">

- Form 사용시 주의 사항
    - 해킹에 취약함
        - CSRF(Cross-Stie request forgery)
            - 장고 서버 자체적으로 session과 csrf token을 만들어 session information에 담고 있고 그 정보를 일정 시간 동안 저장하고 있는다.
            - 해킹을 방지하는 목적으로 사용 됨.


- Code
    - `polls/views.py`
        - detail
        ```
        def detail(request, question_id) :
            try :
                question = Question.objects.get(pk = question_id)
            except Question.DoesNotExist:
                raise Http404("해당 질문을 찾을 수 없습니다.")
            return render(request, "polls/detail.html", {"question" : question})
        ```
            - get_object_or_404 : Query로 select된 데이터를 가져오는데, 자료가 없다면 자체적으로 404 에러 폼을 가져오는 명령어
        - results
        ```
        def results(request, question_id) :
            question = get_object_or_404(Question, pk = question_id)
            return render(request, "polls/results.html", {"question" : question})
        ```
        - vote
        ```
        def vote(request, question_id) :
            question = get_object_or_404(Question, pk = question_id)
            print(question)
            try :
                selected_choice = question.choice_set.get(pk = request.POST["choice"])
            except (KeyError, Choice.DoesNotExist):
                return render(request, "polls/detail.html", {"question" : question, "error_message" : "항목을 선택하지 않았습니다."})

            else :
                selected_choice.votes += 1
                selected_choice.save()
                return HttpResponseRedirect(reverse("polls:results", args = (question_id,)))
        ```
    
    - `polls/templates/polls/results.html`
        ```
        {% extends "base.html" %}
        {% block content %}
        <h1>{{ question.question_text }}</h1>

        <ul>
        {% for choice in question.choice_set.all %}
            <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
        {% endfor %}
        </ul>

        <a href="{% url 'polls:detail' question.id %}">Vote again?</a>
        {% endblock content %}
        ```

    - `polls/templates/polls/detail.html`
    ```
    {% extends "base.html" %}
    {% block content %}
    <form action="{% url 'polls:vote' question.id %}" method="post">
        {% csrf_token %}
        <fieldset>
            <legend><h1>{{ question.question_text }}</h1></legend>
            {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
            {% for choice in question.choice_set.all %}
                <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
                <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
            {% endfor %}
        </fieldset>
        <input type="submit" value="Vote">
        </form>
    {% endblock content %}
    ```

            
