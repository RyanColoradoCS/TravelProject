from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

'''
The Meta class in Django forms is used to specify configurations 
for the form itself—essentially telling the form how it should behave and which model and fields it is associated with
'''


class CustomUserCreationForm(UserCreationForm):
    # Meta class overrides default fields
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age", "car_type")

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
