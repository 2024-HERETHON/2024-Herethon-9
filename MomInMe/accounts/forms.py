from django import forms
from .models import UserProfile


class SignupFirstForm(forms.Form):
    username = forms.CharField(label='아이디', max_length=100)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    terms = forms.BooleanField(label='이용약관 동의', required=True)
    privacy = forms.BooleanField(label='개인정보처리방침 동의', required=True)
    email_opt_in = forms.BooleanField(label='이메일 알림 수신 동의', required=False)

class SignupSecondForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture','baby_id', 'baby_birthdate', 'baby_gender', 'mom_id', 'mom_birthdate']
        widgets = {
            'baby_birthdate': forms.DateInput(attrs={'type': 'date'}),
            'mom_birthdate': forms.DateInput(attrs={'type': 'date'}),
        }
    
    profile_picture = forms.ImageField(label='프로필 사진', required=False)
    baby_id = forms.CharField(label='아기 아이디', max_length=100)
    baby_birthdate = forms.DateField(label='아기 생년월일', widget=forms.DateInput(attrs={'type': 'date'}))
    baby_gender = forms.ChoiceField(label='아기 성별', choices=(('M', '남자'), ('F', '여자')))
    mom_id = forms.CharField(label='엄마 아이디', max_length=100)
    mom_birthdate = forms.DateField(label='엄마 생년월일', widget=forms.DateInput(attrs={'type': 'date'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='사용자 이름', max_length=100)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)