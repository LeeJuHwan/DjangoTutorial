### STEP 18

### FORMS STYLING
- use {% load static %}
- static 디렉터리 만들기
    - polls/static/polls/custom.css

    <img width="973" alt="image" src="https://user-images.githubusercontent.com/118493627/216924435-16677cb1-de91-46f2-abff-9a3d8f106c85.png">

    - Form 렌더링 할 때 키워드 인자를 추가하기
        - widget이 html 컴포넌트로 변환 시켜준다. 
        <img width="987" alt="image" src="https://user-images.githubusercontent.com/118493627/216924770-aa162dca-8edf-4304-a471-da3ac55a574e.png">

- Code
    - widget 추가
        - `polls/forms.py`
            ```
            class SurveyForm(forms.Form):
                user_name = forms.CharField(
                    label="your name", 
                    max_length=100,
                    widget=forms.TextInput(attrs={"class" : "form-control"}))

                user_age = forms.IntegerField(
                    label="your age",
                    widget=forms.NumberInput(attrs={"class" : "form-control"}))
            ```
    - css render
        - `polls/static/polls/polls_custom.css`
            ```
            form {
                border: 1px dotted blue;
                padding: 30px;
                margin: 10px;
            }
            ```

        - `polls/templates/polls/survey_custom.html`
            ```
            {% extends "base.html" %}

            {% load static %}

            {% block content %}
            <link rel="stylesheet" href="{% static 'polls/polls_custom.css' %}" />
            ```
