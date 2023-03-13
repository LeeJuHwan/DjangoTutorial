# STEP 5

## What's API?
<img width="980" alt="image" src="https://user-images.githubusercontent.com/118493627/224306295-73e30782-0a3c-4926-a5cb-2b2856798abc.png">

- API를 만드는 이유
    - 모든 디바이스에서 받는 요청을 한 번에 처리하기 위해 공통적인 인터페이스를 개발자에게 알려주고, 개발자는 공식 문서를 보고 어떤 방향으로 응답을 보내고, 요청을 받는지 확인하는 방법이 된다.

    - 하나의 API를 제대로 만들어두면 Front-end에서 인터페이스를 제너럴한 방식으로 서포트 할 수 있다.

    - 트래픽이 많이 발생하게 되면, API 서버로 트래픽을 서포트 할 수 있고 데이터베이스나 백엔드 부분도 확장이 가능하다.

### API documentation
<img width="905" alt="image" src="https://user-images.githubusercontent.com/118493627/224306395-f3a42add-b230-43b2-bfc2-23867b0c7112.png">
- API를 개발하면, API에 대해 설명을 하기 위해 문서화 해야한다. 나만 알고 있는 API는 만드는 이유가 사라진다. 

### Documentation Content
<img width="812" alt="image" src="https://user-images.githubusercontent.com/118493627/224306803-d90f0bfd-027c-4291-8035-15ec53e6f889.png">

- API Docs 요소
    - method(PUT,GET ...)
    - request format
        - url params(?a=1)
        - html body in data format
    - response format
        - JSON format


### How to make API Documentation?
<img width="933" alt="image" src="https://user-images.githubusercontent.com/118493627/224307501-859e3a91-ea5f-4d05-96e2-da93d5d93909.png">
- 일일히 글을 작성하지 않고, 툴을 사용하여 만들 수 있다.
- Tool
    - DRF-spectacular

### Configuration
<img width="896" alt="image" src="https://user-images.githubusercontent.com/118493627/224307922-943827da-5190-4634-8011-7a16cdfc4698.png">

### set-up
- install
    ```
    pip3 install drf-spectacular
    ```

- `settings.py`
    - Installed apps
        ```
        "rest_framework",
        "drf_spectacular",
        ```    

    - Spectacular settings
        ```
        SPECTACULAR_SETTINGS = {
            'TITLE': 'Learn Python Django API',
            'DESCRIPTION': 'Python Django API',
            'VERSION': '1.0.0',
            'SERVE_INCLUDE_SCHEMA': False,
        }
        ```
    - Rest Framework setting
        ```
        REST_FRAMEWORK = {
            'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
        }
        ```
- `app/urls.py`
    ```
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ```
    - SpectacularSwaggerView
        - swagger UI
    -  SpectacularAPIView
        - API info to yaml for downloads
        