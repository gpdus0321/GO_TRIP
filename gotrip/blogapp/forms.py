from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['제목', '체크리스트1','체크리스트2','체크리스트3', '이미지', '내용']
