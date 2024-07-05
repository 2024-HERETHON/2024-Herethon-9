from django.shortcuts import render

def home(request):
    # 여기에 '/' 경로에 대한 처리 로직을 작성합니다.
    return render(request, 'index.html')  # home.html은 실제로 보여줄 템플릿 파일의 이름입니다.
