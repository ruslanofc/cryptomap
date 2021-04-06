from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from products.models import *


def index(request):
    shopsDescriptions = ShopDescription.objects.all()
    context = {
        'shopsDescriptions': shopsDescriptions,
        'title': 'Список магазинов',
    }
    return render(request, template_name='shops/index.html', context=context)


def get_category(request, category_id):
    shopsDescriptions = ShopDescription.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'shopsDescriptions': shopsDescriptions,
        'category': category
    }

    return render(request, template_name='shops/category.html', context=context)


def view_shops(request, shops_id):
    shops_item = ShopDescription.objects.get(shop_id=shops_id)

    products = Product.objects.filter(shop=shops_id)
    return render(request, 'shops/view_shops.html', {"shops_item": shops_item, "products": products})


def add_shops(request):
    if request.method == 'POST':
        shopsForm = ShopsForm(request.POST)
        if shopsForm.is_valid():
            Shop.objects.create(**shopsForm.cleaned_data)

            return redirect(reverse('add_shops_descriptions'))
    else:
        shopsForm = ShopsForm()
    return render(request, 'shops/add_shops.html', {'shopsForm': shopsForm})


def add_shops_descriptions(request):
    instance = Shop.objects.last()
    if request.method == 'POST':
        shopsDescriptionForm = ShopsDescriptionsForm(request.POST)
        if shopsDescriptionForm.is_valid():
            ShopDescription.objects.create(**shopsDescriptionForm.cleaned_data)

            return redirect('home')
    else:
        shopsDescriptionForm = ShopsDescriptionsForm(initial={'shop': instance.id})
        return render(request, 'shops/add_shops_descriptions.html', {'shopsDescriptionForm': shopsDescriptionForm})

