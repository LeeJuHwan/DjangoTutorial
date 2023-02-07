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

    