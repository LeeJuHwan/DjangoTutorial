from django.urls import path

from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.MainView.as_view(), name = "main"),
    # path("car/", views.CarFormView.as_view(), name = "car") 
    path("create_car/", views.CarCreateView.as_view(), name = "car-create"),
]