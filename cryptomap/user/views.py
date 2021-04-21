from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.forms import RegistrationForm, CustomUserAuthenticationForm, AccountUpdateForm, ContactForm
from django.views.generic import DetailView, View
from .models import CustomUser
from products.models import Product
from django.core.mail import send_mail


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else: #get request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'user/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = CustomUserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user/login.html', context)


def account_view(request):

    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username":request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username
            }
        )
    context['account_form'] = form
    return render(request, 'user/account.html', context)


def contact_form_view(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'cryptomap2021@gmail.com', ['ruslanofcourse@gmail.com'], fail_silently=False)
            if mail:
                messages.add_message(request, messages.INFO, 'Письмо отправлено')
                return redirect('contact_form')
            else:
                messages.add_message(request, messages.INFO, 'Ошибка отправки')
        else:
            messages.add_message(request, messages.INFO, 'Ошибка, заполните все поля')
    else:  # get request
        form = ContactForm()
    return render(request, 'user/contact_form.html', {'form': form})

