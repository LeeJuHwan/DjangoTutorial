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

### ABOUT CODE
- `inventory/views.py`
    - [ADD] class view 
    ```
    class CarListView(ListView) :
    model = Car
    paginate_by = 100

    queryset = Car.objects.filter(brand__iexact = "tesla")
    def get_context_data(self, **kwargs) : 
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    ```

- `inventory/urls.py`
    - [ADD] routing url
    ```
    path("list_car/", views.CarListView.as_view(), name = "car-list"),
    ```

- `inventory/templates/inventory/car_list.html`
    - app / models_list.html 파일명에 맞춰주면 ListView에서 파일을 찾기 때문에 template name을 지정하지 않아도 된다.
    ```
    <h1>Cars</h1>
    <ul>
    {{ now }}
    {% for car in object_list %}
        <li><a href="{% url "inventory:car-detail" car.id %}">{{ car.brand }}: {{ car.model }} {{ car.color }} {{ car.year }}<a/></li>
    {% empty %}
        <li>No cars yet.</li>
    {% endfor %}
    </ul>
    ```
---
## DETAIL VIEW
<img width="1003" alt="image" src="https://user-images.githubusercontent.com/118493627/223461060-b9ac533e-acab-4e82-bafb-76cb84324cb7.png">

- 템플릿에서 상세 페이지에서 정보를 나타낼 때

- `template/app/model_detail.html` 파일명을 권장하고 있다.

<img width="1045" alt="image" src="https://user-images.githubusercontent.com/118493627/223461540-a2d5c384-ae38-440f-8cce-e5968d1f5e4f.png">

- `views.py` 에서는 권장하는 파일명만 맞춰주면 이와 같이 간단하게 사용 할 수 있다.

- 주로 anchor tags를 사용 하여, 템플릿에서 url redirect를 시도하고, detail page에 접근 하는 고유 id를 인자로 넘겨 받아, 해당하는 id의 데이터를 보여줘야 한다.

### ABOUT CODE
- `inventory/views.py`
    ```
    class CarDetailView(DetailView) :
    model = Car
    ```

- `inventory/urls.py`
    - list view에서 car.id로 넘겨 받은 id값을 url에 같이 넘겨줌

    ```
    path("detail_car/<int:pk>", views.CarDetailView.as_view(), name = "car-detail"),
    ```

- `inventory/templates/inventory/car_detail.html`
    ```
    <h1>{{ object.brand }}</h1>
    <p>{{ object.model }}</p>
    <p>{{ object.color }}</p>
    <p>{{ object.year }}</p>
    <a href="{% url "inventory:car-update" car.id %}">Update</a><br />
    <a href="{% url "inventory:car-delete" car.id %}">Delete</a>
    ```
---
## UPDATE VIEW
<img width="1067" alt="image" src="https://user-images.githubusercontent.com/118493627/223623157-6bdf85df-c58e-40f2-9ad0-e98e72c2091c.png">

- Detail View와 Create View의 합성과 같다.
- 현재 존재하는 오브젝트를 수정 할 때 이 폼을 사용할 수 있다.
- 업데이트를 시도 하다 에러가 발생하면 리다이렉션 기능을 지원하고, 성공 하면 오브젝트를 변경 한다.

- Create View에서 사용 된 권장하는 파일명을 Update View에서 재사용 할 수 있다. 
    - e.g -> 
    `template/app/model_form.html`

- 위와 같은 재사용 템플릿을 사용하지 않는다고 하면, 템플릿 파일명을 Class 내부에서 변경 할 수 있다.
    - e.g 
    ```
    template_name_suffix = "_update_form"
    ```
    - 이렇게 설정을 변경하게 되면, Update View에서 템플릿을 참조할 때 `template/app/model_update_form.html` 을 찾게된다.


<br ><img width="1133" alt="image" src="https://user-images.githubusercontent.com/118493627/223624081-400317f3-859d-4937-9925-82ccb12a3884.png">

### ABOUT CODE
- `inventory/urls.py`
    - [ADD]
    ```
    path("update_car/<int:pk>", views.CarUpdateView.as_view(), name = "car-update"),
    ```

- `inventory/views.py`
    - [ADD]
    ```
    class CarUpdateView(UpdateView) : 
    model = Car
    fields = "__all__" # ["brand", "model", "color", "year"]
    success_url = reverse_lazy("inventory:car-list")

    template_name_suffix = "_update_form"
    ```

- `inventory/template/inventory/car_update_form.html`
    ```
    <h1>Update</h1>
    <form method="post">{% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Update message">
    </form>
    ```


## DELETE VIEW
<img width="1050" alt="image" src="https://user-images.githubusercontent.com/118493627/223625300-fcfc4d14-f48e-477d-9e76-e0006fc07725.png">

- Delete View는 데이터를 삭제 하기 전 나타나는 confirmation page가 존재하여 삭제 여부를 체크한다.

- `template/app/model_confirm_delete.html` 파일명을 
권장하고 있지만, Update View와 같이 class 내에서 suffix를 사용하여 템플릿 이름을 변경하여 참조 할 수 있다. 
    - e.g -> `template_name_suffix = "_check_form"`

<img width="1161" alt="image" src="https://user-images.githubusercontent.com/118493627/223626769-0de2d9f7-3413-43b9-b5a3-a32dd77a0437.png">

### ABOUT CODE 
- `inventory/urls.py`
    ```
    path("delete_car/<int:pk>", views.CarDeleteView.as_view(), name = "car-delete")
    ```

- `inventory/views.py`
    ```
    class CarDeleteView(DeleteView) :
    model = Car
    success_url = reverse_lazy("inventory:car-list")
    ```

- `inventory/template/inventory/car_confirm_delete.html`
    ```
    <form method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    {{ form }}
    <input type="submit" value="Confirm">
    </form>
    ```

