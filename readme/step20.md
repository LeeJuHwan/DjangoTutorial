### STEP 20

### CBV
    - FBV가 아닌 왜 CBV여야 하는가?
        - GET, POST 처리 방식을 지정해줘야 하는 함수처리 방식이 있는 반면에 GET, POST 방식을 선언만 해두면 일괄적으로 처리되는 시스템을 이용 할 수 있다.

    - mixin 사용(상속)
        - 함수기반은 여러개를 부를 수 있지만 재사용성이 상대적으로 떨어지기 때문에 클래스 기반을 선호한다.
    - CBV와 FBV

<img width="1132" alt="image" src="https://user-images.githubusercontent.com/118493627/216999764-d38e88b9-2755-4f38-8709-5c394440c88f.png">

    - TEMPLATE VIEW(CBV)
        - template_name에 내용을 지정하고 클래스 내에서 처리할 수 있다.
    
        - kwargs를 언패킹하고, super 상속을 받아서 context 처리

### 새로운 프로젝트 시작

### 환경 설정
- 프로젝트 시작
    - 가상환경 생성 & 활성화
        ```
        python -m venv venv
        source venv/bin/activate
        ```

    - 프로젝트 생성
        ```
        django-admin startproject dealershop
        ```

    - 앱 생성
        ```
        python manage.py startapp inventory
        ```

    - `settings.py`
        ```
        # INSTALLED_APPS 추가
        inventory.apps.InventoryConfig
        ```

### 라우팅 설정
- `dealershop/urls.py`
        ```
        """dealershop URL Configuration
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path("admin/", admin.site.urls),
            path("inventory/", include("inventory.urls"))
        ]

        ```

    - `inventory/urls.py`
        ```
        from django.urls import path

        from . import views

        app_name = "inventory"

        urlpatterns = [
            path("", views.MainView.as_view(), name = "main")
        ]
        ```

### CBV 폼 설정
- `inventory/views.py`
    ```
    from django.shortcuts import render
    from django.http import HttpResponse
    from django.views.generic import TemplateView

    class MainView(TemplateView) :
        template_name = "inventory/main.html"
        
        def get_context_data(self, **kwargs: str) -> dict[str, str]:
            context =  super().get_context_data(**kwargs)
            context["name"] = "Hwany"
            return context
    ```

### 템플릿 렌더링
- `inventory/templates/inventory/main.html`
    ```
    <h1>안녕하새우 {{ name }}씨~ </h1>
    ```