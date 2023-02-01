### STEP 4
- URL NOT FOUND
    - what's `handler 404` ?
        <img width="1746" alt="image" src="https://user-images.githubusercontent.com/118493627/215963131-8de47591-5aea-414a-8a09-d2aa5630c122.png">
        - 페이지를 요청 했을 때 올바르지 못한 접근으로 인하여 에러가 나타나는 페이지를 관리하는 것
        - 위 페이지에서 url을 어떤 방식으로 입력해야 하는지 알려주기 때문에 웹 페이지 해킹에 대한 위험성이 충분하여 에러 페이지를 관리하는 것이 좋다.

    - In setting
        ```
        DEBUG = False
        ALLOWED_HOSTS = [*]
        ```
        - DEBUG = True 일 때 어떤 에러가 났는지, 어디서 에러가 났는지 정보를 알려준다. 이 부분을 외부에 공개 하게 되면 해킹에 위험이 있으니 `False`로 수정하는 것이 좋다.

        - Allowed_hosts = 어디서 유저가 access를 할 것인지, Asterik를 사용하게 되면 유저가 어디서든 접속 할 수 있다. localhost를 사용하고 싶다면 127.0.0.1 을 사용 할 수 있다.

    - code
        - `mysite/urls.py`
            ```
            handler404 = "mysite.views.error_404_view"
            ```

        - `mysite/urls.py`
            ```
            def error_404_view(request, exception) :
                return HttpResponseNotFound("This page is not found!")
            ```

        - `mysite/settings.py`
            ```
            DEBUG = False
            ALLOWED_HOSTS = ['*']
            ```

        <img width="372" alt="image" src="https://user-images.githubusercontent.com/118493627/215964148-21ff01ca-7aac-4657-9215-8600da8146f0.png">

- REDIRECT
    - Django에서 지원 하는 HttpResponseRedirect를 사용 하여 리다이렉션 할 수 있다.
    - http status code 302
        - redirection http status code

    <img width="2023" alt="image" src="https://user-images.githubusercontent.com/118493627/215965070-59e0f695-459a-4518-ae80-ae3142d4ff1c.png">

    - code
        ```
        def index(request):
            return HttpResponseRedirect("1")
        ```
        <img width="567" alt="image" src="https://user-images.githubusercontent.com/118493627/215965785-9ee1e7d6-5b00-4f6e-b5d9-6dd9c9e51d90.png">

        - 리다이렉션 되는 http status code가 302가 등장하고, 다음으로 polls/1/으로 리다이렉션 된 후 http status code 200을 return 한다