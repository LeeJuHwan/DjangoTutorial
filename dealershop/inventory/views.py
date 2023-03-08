from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView,  CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView


from .forms import CarForm
from .models import Car
from django.utils import timezone

class MainView(TemplateView) :
    template_name = "inventory/main.html"
    
    def get_context_data(self, **kwargs: str) -> dict[str, str]:
        context =  super().get_context_data(**kwargs)
        context["name"] = "Hwany"
        return context
        
# class CarFormView(FormView) :
#     template_name = "inventory/car_basic_form.html"
#     form_class = CarForm
#     success_url = reverse_lazy("inventory:main")

#     def form_valid(self, form) :
#         form.submit()
#         print("cleaned : ", form.cleaned_data)
#         return super().form_valid(form)

class CarCreateView(CreateView) :
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("inventory:car-list")

    def form_valid(self, form) : 
        print(form.cleaned_data)
        return super().form_valid(form)

class CarListView(LoginRequiredMixin, ListView) :
    model = Car
    paginate_by = 100

    queryset = Car.objects.filter(brand__iexact = "tesla")
    def get_context_data(self, **kwargs) : 
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

class CarDetailView(DetailView) :
    model = Car

class CarUpdateView(UpdateView) : 
    model = Car
    fields =  ["brand", "model", "color", "year"]
    success_url = reverse_lazy("inventory:car-list")

    template_name_suffix = "_update_form"

class CarDeleteView(DeleteView) :
    model = Car
    success_url = reverse_lazy("inventory:car-list")


