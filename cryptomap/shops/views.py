from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.core.paginator import Paginator
from .models import *
from products.models import *
from django.views.generic import ListView, DetailView


class CityFilter:
    def get_city(self):
        years_sorted_list = sorted(set(Shop.objects.all().values_list('city', flat=True)))
        return years_sorted_list


class FilterCityShopView(ListView, CityFilter):

    model = ShopDescription
    template_name = "shops/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['shopsDescriptions'] = Shop.objects.filter(city__in=self.request.GET.getlist('city'))

        return context


def search(request):

    shop = Shop.objects.get(title__icontains=request.GET.get('q'))
    shop_item = ShopDescription.objects.get(shop_id=shop.id)
    products = Product.objects.filter(shop=shop.id)
    return render(request, 'shops/view_shops.html', {"shop": shop_item, "products": products})


class AllShopsView(ListView, CityFilter):

    model = ShopDescription
    queryset = ShopDescription.objects.all()
    paginate_by = 3
    context_object_name = 'shopsDescriptions'
    template_name = 'shops/index.html'


class ShopByCategory(DetailView):

    model = ShopDescription
    pk_url_kwarg = 'category_id'
    paginate_by = 1
    template_name = 'shops/category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])
        context['shopsDescriptions'] = ShopDescription.objects.filter(category_id=self.kwargs['category_id'])
        return context


class ViewShop(DetailView):

    model = ShopDescription
    pk_url_kwarg = 'shops_id'
    template_name = 'shops/view_shops.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = ShopDescription.objects.get(shop_id=self.kwargs['shops_id'])
        context['products'] = Product.objects.filter(shop=self.kwargs['shops_id'])
        return context


def view_users_shops(request):
    user = CustomUser.objects.get(username=request.user.username)
    shops = Shop.objects.filter(owner=user)
    context = {
        'shops': shops,
    }
    return render(request, template_name='shops/view_users_shops.html', context=context)


def add_shops(request):
    user = CustomUser.objects.get(username=request.user.username)
    if request.method == 'POST':
        shopsForm = ShopsForm(request.POST)
        if shopsForm.is_valid():
            Shop.objects.create(**shopsForm.cleaned_data)
            return redirect(reverse('add_shops_descriptions'))
    else:
        shopsForm = ShopsForm(initial={'owner': user})
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

