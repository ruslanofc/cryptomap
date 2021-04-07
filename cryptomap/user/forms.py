from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Почта")

    class Meta:
        model = CustomUser
        fields = ("email", "username", "password1", "password2")
