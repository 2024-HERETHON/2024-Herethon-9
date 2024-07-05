# accounts 애플리케이션의 urls.py

from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('mainpage/', views.home, name='home'),  # 첫 번째 회원가입 폼
]
