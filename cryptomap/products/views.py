from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def view_product(request, product_id):
    products = Product.objects.get(pk=product_id)
    products_descriptions = ProductDescription.objects.get(product_id=product_id)

    return render(request, 'products/view_product.html', {"products": products, "products_descriptions": products_descriptions})


# def view_all_products(request):
#     context = {
#         'title': 'Все товары',
#     }
#     return render(request, template_name='products/all_products_by_category.html', context=context)


def get_products_by_category(request, category_id):
    productsDescriptions = ProductDescription.objects.filter(category_id=category_id)
    category = ProductCategory.objects.get(pk=category_id)
    context = {
        'productsDescriptions': productsDescriptions,
        'category': category
    }

    return render(request, template_name='products/all_products_by_category.html', context=context)