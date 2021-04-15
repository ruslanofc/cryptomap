from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.forms import RegistrationForm, CustomUserAuthenticationForm, AccountUpdateForm
from django.views.generic import DetailView, View
from .models import CustomUser, UserTrackedItems
from products.models import Product

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


class UserTrackedItemsView(View):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(username=request.user.username)
        items = UserTrackedItems.objects.get(owner=user)

        return render(request, 'user/tracked_items.html', {'items': items})


class AddToTrackedItemsView(View):
    def get(self, request, product_id, *args, **kwargs):
        customer = CustomUser.objects.get(username=request.user.username)
        trackedItems = UserTrackedItems.objects.get(owner=customer)
        product = Product.objects.get(pk=product_id)
        trackedItems.products.add(product)

        return redirect('tracked_items')