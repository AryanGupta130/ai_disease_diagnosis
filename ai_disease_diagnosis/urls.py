# ai_disease_diagnosis/urls.py

from django.contrib import admin
from django.urls import path
from diagnosis import views  # Ensure this import is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Home page
    path('upload/', views.upload_image, name='upload_image'),  # Image upload page
    path('about/', views.about_tb, name='about_tb'),
]
