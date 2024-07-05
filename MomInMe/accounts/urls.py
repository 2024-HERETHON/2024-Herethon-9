# accounts 애플리케이션의 urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_first, name='signup'),  # 첫 번째 회원가입 폼
    path('setup/', views.signup_second, name='setup'),  # 두 번째 설정 폼
    path('login/', views.user_login, name='login'),
]
