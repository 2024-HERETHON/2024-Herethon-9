# accounts 애플리케이션의 urls.py

from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.home, name='home'),  # 로딩 후 보여지는 페이지
]
