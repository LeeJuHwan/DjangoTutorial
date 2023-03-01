### STEP 1

### FormView
<img width="1165" alt="image" src="https://user-images.githubusercontent.com/118493627/222075430-cc373015-e228-416c-81f7-e0733e4b6209.png">

- success url : Form action에서 form_valid에 정상적인 접근 후 처리가 완료 된 다음 이동 할 라우팅
- formview는 modelform 처럼, `models.py`에 접근하지 않아도 forms 내부에서 같은 코드로 db를 구축 할 수 있다.
- formview 코드 내부에서 커스터마이징한 함수를 정상적인 submit 이후 호출 할 수 있다.

### ABOUT CODE

- `inventory/urls.py`
    - 라우팅 추가
    ```
    urlpatterns = [
        path("", views.MainView.as_view(), name = "main"),
        path("car/", views.MainView.as_view(), name = "main")
    ]
    ```

- `inventory/forms.py`
    - form class 생성
    ```
    from django import forms

    class CarForm(forms.Form) :
        brand = forms.CharField()
        model = forms.CharField()
        color = forms.CharField()
        year = forms.IntegerField()

            def submit() :
                print("submit is POST!")
    ```

- `inventory/views.py`
    - 입력 받은 데이터 처리하는 기능 추가
    ```
    class CarFormView(FromView) :
        template_name = "inventory/car_basic_form.html"
        form_class = CarForm
        success_url = "/inventory"

        def form_valid(self, form) :
            form.submit()
            print(form.cleaned_data)
            return super().form_valid(form)
    ```
- `inventory/templates/car_basic.html`
    - 템플릿 추가
    ```
    <form action="" method = "post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send Message">
    </form>
    ```

### KEYWORD
- FBVs의 reverse vs CBVs의 reverse_lazy()
    - reverse는 string 형태로 return하여, FBVs형태 일 때는 어떠한 문제가 없지만 CBVs에서는 서로 순회 호출 하게 되어 없는 데이터를 Parsing 하려 하는 상황이 발생하기 때문에 에러가 나타나며 사용이 불가능하다.
    - 그 반면, reverse_lazy는 object 형태로 return 하게 되어 string 형태로 Parsing을 하지 않고, object가 url이 렌더링 될 때 필요한 순간 호출이 되기 때문에 문제 없이 사용할 수 있다.


- form.cleaned_data 
    - 입력 받은 데이터를 딕셔너리 형태로 출력한다. 

### SUMMARY 
- FBVs에서는 reverse를 호출 하면 즉시 호출이 가능하다.
- CBVs는 Class 내부의 속성 값을 읽어야 하지만, 입력 된 값이 로딩 되어 있지 않기 때문에 reverse_lazy를 사용





