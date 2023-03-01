from django import forms
from django.db import models

class CarForm(forms.Form) :
    brand = forms.CharField()
    model = forms.CharField()
    color = forms.CharField()
    year = forms.IntegerField()

    def submit(self) :
        print("submit is POST!")