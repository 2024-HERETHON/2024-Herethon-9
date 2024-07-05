from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

@login_required
def home(request):
    # 현재 로그인한 사용자 객체
    user = request.user
    # 사용자의 UserProfile 가져오기
    user_profile = UserProfile.objects.get(user=user)
    
    return render(request, 'home.html', {'user': user, 'user_profile': user_profile})
