from django.shortcuts import render
from django.http import HttpResponse

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