from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView


class ShopCategories:

    def get_shop(self):
        years_sorted_list = sorted(set(Shop.objects.all().values_list('title', flat=True)))
        return years_sorted_list

    def get_categories(self):
        category_sorted_list = sorted(set(ProductCategory.objects.all().values_list('title', flat=True)))
        return category_sorted_list


class FilterShopCategoryView(ListView, ShopCategories):
    model = ProductDescription
    template_name = 'products/all_products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductDescription.objects.all()
        if "shop" in self.request.GET:
            context['products'] = context['products'].filter(product_id__in=Product.objects.values_list('id', flat=True).filter(
                shop_id__in=Shop.objects.values_list('id', flat=True).filter(title__in=self.request.GET.getlist('shop'))))

        if "category" in self.request.GET:
            context['products'] = context['products'].filter(category_id__in=ProductCategory.objects.values_list('id', flat=True).filter(title__in=self.request.GET.getlist('category')))

        context['shopsDescriptions'] = ShopDescription.objects.all()
        return context


def searchProduct(request):

    products = Product.objects.get(title__icontains=request.GET.get('q'))
    products_descriptions = ProductDescription.objects.get(product_id=products.id)

    return render(request, 'products/view_product.html', {"products_descriptions": products_descriptions, "products": products})


class ProductDetailView(DetailView):

    model = Product
    pk_url_kwarg = 'product_id'
    template_name = 'products/view_product.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_descriptions'] = ProductDescription.objects.get(product_id=self.kwargs['product_id'])
        return context


class ProductsView(ListView, ShopCategories):

    paginate_by = 3
    model = ProductDescription
    template_name = 'products/all_products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopsDescriptions'] = ShopDescription.objects.all()
        return context


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