from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_first, name='signup'),  # 첫 번째 회원가입 폼
    path('setup/', views.signup_second, name='setup'),  # 두 번째 설정 폼
    path('login/', views.user_login, name='login'),
    path('baby_keyword/', views.baby_keyword, name='baby_keyword'),
    path('me_keyword/', views.me_keyword, name='me_keyword'),
    path('loading/', views.loading, name='loading'),
]
