from django import forms
from .models import UserPost
from accounts.models import CustomUser

class PostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['title', 'content']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Use the custom user model here
        fields = ['username', 'age']