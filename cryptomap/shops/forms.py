from django import forms
from .models import *


class ShopsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название магазина')
    city = forms.CharField(max_length=60, label='Город')
    address = forms.CharField(max_length=300, label='Адрес магазина')
    latitude = forms.DecimalField(max_digits=10, decimal_places=6, label='Широта')
    longitude = forms.DecimalField(max_digits=10, decimal_places=6, label='Долгота')
    is_published = forms.BooleanField(label='Опубликовать после заполнения', initial=True)


class ShopsDescriptionsForm(forms.Form):
    shop = forms.ModelChoiceField(queryset=Shop.objects.all(), widget=forms.Select(attrs={'readonly': 'readonly'}))
    description = forms.CharField(label='Описание магазина', required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория магазина', empty_label='Выберите категорию')
    email = forms.EmailField(max_length=300, label='Email', required=False)
    url = forms.URLField(max_length=300, label='Ссылка', required=False)
    telegram_url = forms.URLField(max_length=300, label='Telegram', required=False)
    pay_in_rub = forms.BooleanField(label='Прием платежей в рублях', initial=True)
    pay_in_btc = forms.BooleanField(label='Прием платежей в биткоинах', initial=True)



