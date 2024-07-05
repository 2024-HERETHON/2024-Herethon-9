from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'location', 'music_url', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'post-text', 'placeholder': '문구를 작성해 주세요.'}),
            'location': forms.TextInput(attrs={'placeholder': '위치 추가'}),
            'music_url': forms.TextInput(attrs={'placeholder': '음악 추가'}),
        }
