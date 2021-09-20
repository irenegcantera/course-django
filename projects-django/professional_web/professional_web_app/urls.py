from django.urls import path
from professional_web_app import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('career/', views.career, name="Career"),
    path('services/', views.service, name="Services"),
    path('portfolio/', views.portfolio, name="Portfolio"),
    path('news/', views.news, name="News"),
    path('contact/', views.contact, name="Contact"),
]