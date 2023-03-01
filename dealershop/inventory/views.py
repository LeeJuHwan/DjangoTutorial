from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import CarForm

class MainView(TemplateView) :
    template_name = "inventory/main.html"
    
    def get_context_data(self, **kwargs: str) -> dict[str, str]:
        context =  super().get_context_data(**kwargs)
        context["name"] = "Hwany"
        return context
        
class CarFormView(FormView) :
    template_name = "inventory/car_basic_form.html"
    form_class = CarForm
    success_url = reverse_lazy("inventory:main")

    def form_valid(self, form) :
        form.submit()
        print("cleaned : ", form.cleaned_data)
        return super().form_valid(form)

