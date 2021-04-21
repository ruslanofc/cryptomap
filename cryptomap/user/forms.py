from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Почта")

    class Meta:
        model = CustomUser
        fields = ("email", "username", "password1", "password2")


class CustomUserAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login or password")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError('Email {} is alredy in use.'.format(account))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError('Username {} is alredy in use.'.format(username))


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема (впишите почту)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))