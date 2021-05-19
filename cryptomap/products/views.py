from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.views.generic.list import ListView


def view_product(request, product_id):
    products = Product.objects.get(pk=product_id)
    products_descriptions = ProductDescription.objects.get(product_id=product_id)

    return render(request, 'products/view_product.html', {"products": products, "products_descriptions": products_descriptions})


class ProductsView(ListView):

    model = Product
    queryset = Product.objects.all()
    paginate_by = 2


class ProductsByCategory(ListView):
    model = ProductDescription
    template_name = 'products/all_products_by_category.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductDescription.objects.filter(pk=self.kwargs['category_id'])
        context['shopsDescriptions'] = ShopDescription.objects.all()
        return context

    def get_queryset(self):
        return ProductDescription.objects.filter(category_id=self.kwargs['category_id'])


# def get_products_by_category(request, category_id):
#     # для вывода информации о продукте
#     productsDescriptions = ProductDescription.objects.filter(category_id=category_id)
#
#     # для вывода тайтла
#     category = ProductCategory.objects.get(pk=category_id)
#
#     # контекст для кнопки перехода в магазин
#     shopsDescriptions = ShopDescription.objects.all()
#
#     paginator = Paginator(productsDescriptions, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     context = {
#         # 'productsDescriptions': productsDescriptions,
#         'page_obj': page_objects,
#         'category': category,
#         'shopsDescriptions': shopsDescriptions
#     }
#
#     return render(request, template_name='products/all_products_by_category.html', context=context)


def add_product(request, shop_id):
    shop = Shop.objects.get(pk=shop_id)
    if request.method == 'POST':
        productsForm = ProductsForm(request.POST)
        if productsForm.is_valid():
            Product.objects.create(**productsForm.cleaned_data)
            return redirect(reverse('add_product_description'))
    else:
        productsForm = ProductsForm(initial={'shop': shop})
    return render(request, 'products/add_product.html', {'productsForm': productsForm, 'shop_id': shop_id})


def add_product_description(request):
    instance = Product.objects.last()
    if request.method == 'POST':
        productsDescriptionsForm = ProductsDescriptionsForm(request.POST, request.FILES)
        if productsDescriptionsForm.is_valid():
            ProductDescription.objects.create(**productsDescriptionsForm.cleaned_data)

            return redirect('home')
    else:
        productsDescriptionsForm = ProductsDescriptionsForm(initial={'product': instance.id})
        return render(request, 'products/add_product_description.html', {'productsDescriptionsForm': productsDescriptionsForm})