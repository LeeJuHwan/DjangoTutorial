from django import forms

class SurveyForm(forms.Form):
    user_name = forms.CharField(
        label="your name", 
        max_length=100,
        widget=forms.TextInput(attrs={"class" : "form-control"}))

    user_age = forms.IntegerField(
        label="your age",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))