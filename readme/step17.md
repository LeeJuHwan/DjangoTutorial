### STEP 17

### Forms
- html에서 처리하는 form들을 template화 한 과정
    
    <img width="1070" alt="image" src="https://user-images.githubusercontent.com/118493627/216912468-748af648-a334-47a8-bb34-b0450a23328e.png">

    - Forms를 관리하게 되면 HTML에서 하드코드를 할 필요가 많이 줄어든다.
    - is_valid() : validation rule을 확인하고 데이터를 boolean 형태로 return 하고, cleaned_data로 옮겨준다. 자료 형태는 딕셔너리 형태로 저장되어 있음

    - forms rendering
        - Form 클래스에서 지정한 태그 치환
        <img width="1049" alt="image" src="https://user-images.githubusercontent.com/118493627/216913180-b7cb3545-25d6-4956-832a-0443f9fb10e1.png">

- Code
    - `polls/forms.py`
        ```
        from django import forms

        class SurveyForm(forms.Form):
            user_name = forms.CharField(label="your name", max_length=100)
            user_age = forms.IntegerField(label="your age")
        ```

    - `polls/urls.py` [일부 추가]
        ```
        # /polls/survey/
        path("survey/", views.survey, name = "survey"),
        path("thanks/", views.thanks, name = "thanks")
        ```

    - `polls/views.py`
        ```
        def survey(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = SurveyForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                print(form.cleaned_data["user_name"])
                print(form.cleaned_data["user_age"])
                return HttpResponseRedirect(reverse("polls:thanks"))

        # if a GET (or any other method) we'll create a blank form
        else:
            form = SurveyForm()

        return render(request, "polls/survey_custom.html", {"form" : form})

    def thanks(request) :
        return render(request, "polls/thanks.html", {})
        ```

    - `polls/templates/polls/survey_custom.htl`
        ```
        {% extends "base.html" %}
        {% block content %}
        <form action="{% url 'polls:survey' %}" method = "post">
            {% csrf_token %}
            <!-- {{ form.as_div }} -->
            
            {{ form.user_name.label_tag }} {{ form.user_name }}
            {{ form.user_age.label_tag }} {{ form.user_age }}

            <!-- {{ form.user_name.errors }}
            <label for="{{ form.user_name.id_for_label}}">User name :</label>
            {{ form.user_name }} -->

            <!-- {% for field in form %}
            <div class="fieldWrapper">
                {{field.errors}}
                {{field.label_tag}} {{field}}
                {% if field.help_text %}
                <p class="help">{{ field.help_text | safe }}</p>
                {% endif %}
            </div>
            {% endfor %} -->
            <input type="submit" value="Submit">
        </form>
        {% endblock content %}
        ```

