# DjangoTutorial
API practice 

## Django pracitce

### STEP 1
- 가상환경 설정

    ```
    python -m venv ./venv
    ```

    ```
    [shell] vim activate

    source venv/bin/activate
    ```


- Django run
    ```
    django-admin startproject mysite
    ```

    ```
    python manage.py runserver
    ```

- Django admin page
    <img width="947" alt="image" src="https://user-images.githubusercontent.com/118493627/215752034-a7292981-a21d-4983-89c5-739e3c57138d.png">

### STEP 2
[참고자료](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
- principle
    <img width="948" alt="image" src="https://user-images.githubusercontent.com/118493627/215752901-043a201f-7052-412c-8644-7bd1ba749c43.png">

- create polls app
    ```
    python manage.py startapp polls
    ```
    <img width="359" alt="image" src="https://user-images.githubusercontent.com/118493627/215755057-91f6327b-bf85-4f1f-baa0-2fe45f1b086c.png">

- index page routing
    `views.py`

    ```
    from django.http import HttpResponse

    def index(request):
    return HttpResponse("Hello, My first App.")

    ```

    - `urls.py`

    ```
    from django.urls import path

    from . import views

    urlpatterns = [
    path('', views.index, name = 'index')
    ]
    ```

    - [EDIT] mysite/views.py

    ```
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
    path('polls/', include('polls.urls')),
    path("admin/", admin.site.urls),
    ]
    ```

### STEP 3

- what's urls.py?

    - 장고에서 사용자가 웹 주소를 입력하여 GET 방식으로 서버에 요청을 보낼 때 응답하는 함수가 라우팅 되는 곳이다.

    ```
    from django.urls import path

    from . import views

    urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/results', views.results, name = 'results'),
    path('<int:question_id>/vote', views.vote, name = 'vote')
    ]
    ```

    - params
        - path(route, view_function(callable), variable_name)
        - like this.

            ```
            path('{route}', {views_function}, name = {variable_name})
            ```
- what's views.py?

    - 호출이 가능한 객체, 즉 요청 방식을 지정하고 어떤 값을 return 하는지 결정하는 곳이다.

    - FBVs(function-based-views)

        - 매우 간단한다
        - 내용을 추가 하거나, 재사용성이 떨어진다.
        - 복잡한 구문을 작성할 때 Django프레임워크의 소스코드 까지 봐야 할 때 사용한다.

        - template을 지정하여 return을 함수에서 처리하는 방식이며 이러한 방식을 사용 했을 때의 단점은 들어오는 methods를 각 각 처리 해줘야 하는 번거로움이 있다.

        <img width="428" alt="image" src="https://user-images.githubusercontent.com/118493627/215936604-b3519809-1847-4541-a1cc-15c601842bd2.png">
    
    - CBVs(class-based-views)

        - 반복되는 코드를 피할 수 있다.
        - Django에서 generic view를 지원 하기 때문에 패턴화(간단한) 코드를 사용 할 때 편리하다.
        - CRUD를 사용할 때 많이 이용되는 방식이다.

        <img width="408" alt="image" src="https://user-images.githubusercontent.com/118493627/215937599-231cd6f0-62c2-4afb-8103-a4b08616d926.png">

- polls redirection
    - 위에 `urls.py` 와  `views.py` 를 배웠으니 응용하여 코드를 작성하고 페이지를 출력한다.
    - `polls/views.py`
        ```
        from django.http import HttpResponse


        def index(request):
            return HttpResponse("polls index")

        def detail(request, question_id) :
            return HttpResponse(f"looking at question_id page {question_id}.")

        def results(request, question_id) :
        response = "Yoe're looking at the results of question %s."
            return HttpResponse(response % question_id)

        def vote(request, question_id) :
            return HttpResponse(f"looking at voting at question page {question_id}.")
        ```
    <img width="393" alt="image" src="https://user-images.githubusercontent.com/118493627/215937745-1ccca4c2-62a5-4a10-80f7-b4c9964e39bb.png">

    <img width="385" alt="image" src="https://user-images.githubusercontent.com/118493627/215938194-1e44d66a-6452-4e31-a1b3-0d3216abc60d.png">
