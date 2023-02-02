### STEP 9

- ERROR PAGE
    - 404.html or 500.html

    - Update settings.py
        - DEBUG = False
        - Allowed_host = ['*']

    - 클라이언트의 잘못된 요청 에러인 http status 404 code와 서버 에러인 500 code를 Template을 통해 관리할 수 있다. 이 전에 배운 에러 페이지는 템플릿을 렌더링 한 것이 아닌 에러문을 출력 했기 때문에 복잡한 시스템에서는 템플릿에서 관리 해주는 것이 좋다.

- code
    - `mysite/templates/404.html`
        ```
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>404 Error</title>
        </head>
        <body>
            404 Error    
        </body>
        </html>
        ```

    - `mysite/templates/500.html`
        ```
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>505 Error</title>
        </head>
        <body>
            500 Error    
        </body>
        </html>
        ```

    - `mysite/urls.py`
        ```
        handler404 = "mysite.views.error_404_view"

        handler500 = "mysite.views.error_500_view"
        ```
        - urls.py에서 handler404, handler500 변수를 주석 처리 하여도 에러 페이지는 정상 작동한다. 그 이유는, 폴더 구조에서 templates가 글로벌 환경에 있기 때문에 404.html을 렌더링 하는 과정이 이루어진다. 

        - 그래도 이 변수를 받아서 사용하는 이유는, 에러에 대한 context를 template을 통해 날리고 싶을 때 사용 할 수 있다.

        <img width="427" alt="image" src="https://user-images.githubusercontent.com/118493627/216059521-2642eb1c-50da-471a-8e8a-a8603fe8e0d8.png">



    - `mysite/views.py`
        ```
        from django.http import HttpResponse, HttpResponseNotFound
        from django.shortcuts import render
        def index(request) :
            return HttpResponse("main index")

        def error_404_view(request, exception) :
            # return HttpResponseNotFound("This page is not found!")
            return render(request, "404.html")

        def error_500_view(request) : 
            return render(request, "500.html")
        ```

    