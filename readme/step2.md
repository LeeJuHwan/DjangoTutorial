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