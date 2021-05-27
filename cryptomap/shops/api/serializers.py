from rest_framework import serializers
from rest_framework.filters import SearchFilter
from ..models import Category, Shop, ShopDescription, CustomUser


class CategorySerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = [
            'id', 'title'
        ]


class ShopSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects)
    title = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    latitude = serializers.DecimalField(max_digits=10, decimal_places=6, required=True)
    longitude = serializers.DecimalField(max_digits=10, decimal_places=6, required=True)
    created_at = serializers.DateTimeField(required=True)
    updated_at = serializers.DateTimeField(required=True)
    is_published = serializers.BooleanField(required=True)

    class Meta:
        model = Shop
        fields = '__all__'


class ShopDescriptionSerializer(serializers.ModelSerializer):
    shop = serializers.PrimaryKeyRelatedField(queryset=Shop.objects)
    description = serializers.CharField(required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    photo = serializers.ImageField(required=True)
    email = serializers.EmailField(required=True)
    url = serializers.URLField(required=True)
    telegram_url = serializers.URLField(required=True)
    pay_in_rub = serializers.BooleanField(required=True)
    pay_in_btc = serializers.BooleanField(required=True)

    class Meta:
        model = ShopDescription
        fields = '__all__'

