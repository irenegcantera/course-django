from django.urls import path
from servicesapp import views

urlpatterns = [
    path('', views.service, name="Services"),
]
