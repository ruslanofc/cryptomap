from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView


class PriceCity:

    def get_price_btc(self):
        return Shop.objects.all()

    def get_price_rub(self):
        return Shop.objects.all()


class ProductDetailView(DetailView):

    model = Product
    pk_url_kwarg = 'product_id'
    template_name = 'products/view_product.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_descriptions'] = ProductDescription.objects.get(product_id=self.kwargs['product_id'])
        return context


class ProductsView(ListView, PriceCity):

    model = Product
    queryset = Product.objects.all()
    paginate_by = 2


class ProductsByCategory(ListView):

    model = ProductDescription
    template_name = 'products/all_products_by_category.html'
    context_object_name = 'products'
    paginate_by = 2
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductDescription.objects.filter(pk=self.kwargs['category_id'])
        context['shopsDescriptions'] = ShopDescription.objects.all()
        return context

    def get_queryset(self):
        return ProductDescription.objects.filter(category_id=self.kwargs['category_id'])


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