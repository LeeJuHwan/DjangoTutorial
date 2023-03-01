# STEP 2

## CREATE VIEW
<img width="1174" alt="image" src="https://user-images.githubusercontent.com/118493627/222211871-1a035073-b45f-4465-a63a-ffb90787bef0.png">

- template name : `templates/app/model_form.html` 파일명을 권장함
- Create View는 오브젝트를 생성하고 저장하는 역할을 한다.
---
### ABOUT CODE
- `inventory/views.py`
    ```
    class CarCreateView(CreateView) :
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("inventory:main")

    def form_valid(self, form) : 
        print(form.cleaned_data)
        return super().form_valid(form)
    ```

- `inventory/urls.py`
    ```
    path("create_car/", views.CarCreateView.as_view(), name = "car-create"),
    ```
    <img width="796" alt="image" src="https://user-images.githubusercontent.com/118493627/222221837-d7a9ab80-0e15-40c0-baea-5d25cb7fd3c1.png">
---
## LIST VIEW
<img width="1017" alt="image" src="https://user-images.githubusercontent.com/118493627/222222172-4bb73697-14cd-4fbe-9541-2215b7868a4f.png">

- 일반적으로 게시판의 게시글 리스트 템플릿 형태에 많이 사용 되며, 어드민 페이지에서 확인이 가능했던 데이터를 템플릿 내에서 볼 수 있다.

- `template/app/model_list.html` 파일명을 권장하고 있다. 파일명이 다를 경우, template name을 별도로 지정 해줘야 하는 경우가 있지만, 형식에 맞춰 작성 한다면 파일명이 있는지 검사 하기 때문이다.

- 모델이 접근할 때는 object_list __method__를 활용 하여 접근할 수 있고, query set으로 커스터마이징한 데이터를 가져올 수도 있다.
    <img width="1201" alt="image" src="https://user-images.githubusercontent.com/118493627/222223735-cf1fc55f-4c63-425a-a170-2f600a5f798f.png">
    - object_list -> car_list 로 변경할 수 있다.
    - queryset을 통해 데이터를 가져올 수 있으며, all을 기본으로 사용 하지만 filter를 통해 tesla가 있는 데이터만 추출한 코드를 작성 하였다.
    - get_context_data 라는 optional 함수를 통해 템플릿에 보내 줄 데이터를 딕셔너리 형태로 추가 하였다.


