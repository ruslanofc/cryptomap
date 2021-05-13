from django import forms
from .models import *
from user.models import CustomUser
from shops.models import Shop


class ProductsForm(forms.Form):
    shop = forms.ModelChoiceField(queryset=Shop.objects.all(), label='Магазина', widget=forms.Select(attrs={'readonly': 'readonly'}))
    title = forms.CharField(max_length=150, label='Название товара')
    price_rub = forms.DecimalField(max_digits=20, decimal_places=7, label='Цена в рублях')
    price_btc = forms.DecimalField(max_digits=20, decimal_places=7, label='Цена в биткоинах')
    is_published = forms.BooleanField(label='Опубликовать после заполнения', initial=True)


class ProductsDescriptionsForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(attrs={'readonly': 'readonly'}))
    description = forms.CharField(label='Описание товара', required=False)
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), label='Категория товара', empty_label='Выберите категорию')



