from django.urls import path
from newsapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news, name="News"),
    path('category/<int:category_id>/', views.category, name="Category"),
]