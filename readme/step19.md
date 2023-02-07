### STEP 19

### MODEL FORM
- 모델에서 HTML이 자동으로 생성된다.

    <img width="840" alt="image" src="https://user-images.githubusercontent.com/118493627/216935114-44220e6d-2667-46e0-9f87-d8f250e26452.png">

    <img width="1014" alt="image" src="https://user-images.githubusercontent.com/118493627/216935553-e6d47b5e-a2d9-4b7a-ad5a-13773091b3c2.png">

    - Modelform 에서 가장 중요한 부분!
        - form.save()
            - 데이터베이스를 저장 시킬 수 있다.

### MODEL FORM STYLING
- 필드를 optional이 아닌 전체를 지정할 때
    - `fileds = '__all__'`

    - model form의 label을 수정해서 Return 할 때 
    ```
    labels = {
        "user_name" : "User Name",
        "user_age" : "User Age"
    }
    ```

    - widget도 딕셔너리 형태의 인자로 지원한다.

- Code
    - Model 추가
        - `polls/models.py`
            ```
            class Survey(models.Model) :
                user_name = models.CharField(max_length = 200)
                user_age = models.IntegerField(
                    validators=[
                        MinValueValidator(1),
                        MaxValueValidator(100)])
                        
                def __str__(self) :
                    return f"{self.user_name}_{self.user_age}" 
            ```

    - views 함수 수정
        - `polls/views.py`
            ```
            def survey(request):
            
                if request.method == 'POST':
                
                    form = SurveyForm(request.POST)
                    if form.is_valid():

                        #update
                        # survey = Survey.objects.get(pk = 1)
                        # form = SurveyForm(request.POST, instance = survey)
                        form.save()
                        return HttpResponseRedirect(reverse("polls:thanks"))
                else:
                    form = SurveyForm()

                return render(request, "polls/survey_custom.html", {"form" : form})
            ```
    
    - Model Forms 추가
        - `polls/forms.py`
            ```
            from django.forms import ModelForm, TextInput, NumberInput, forms
            from polls.models import Survey

            class SurveyForm(ModelForm):
                class Meta:
                    model = Survey
                    fields = "__all__"
                    labels = {
                        "user_name" : "User Name",
                        "user_age" : "User Age"
                    } 
                    widgets = {
                        "user_name" : TextInput(attrs={"class" : "form-control"}),
                        "user_age" : NumberInput(attrs={"class" : "form-control"})
                    }
            ```
    - Admin db 추가
        - `polls/admin.py`
            ```
            admin.site.register(Survey)
            ```

    - migrantion
        ```
        python manage.py makemigrations
        python manage.py migrate
        ```

