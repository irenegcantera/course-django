from django.urls import path
from professional_web_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('career/', views.career, name="Career"),
    path('portfolio/', views.portfolio, name="Portfolio"),
    path('news/', views.news, name="News"),
    path('contact/', views.contact, name="Contact"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)