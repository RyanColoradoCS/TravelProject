from django import forms
from .models import UserPost

class PostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['content']