from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields="image","status","bio"


class MyUserCreationForm(UserCreationForm):
    email=forms.EmailField(required=True,help_text="Please enter your email")
    class Meta(UserCreationForm.Meta):
        model=User
        fields=UserCreationForm.Meta.fields+("email",)