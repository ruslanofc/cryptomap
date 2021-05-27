from rest_framework import serializers
from rest_framework.filters import SearchFilter
from ..models import ProductCategory, Product, ProductDescription, CustomUser


class ProductsCategorySerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True)

    class Meta:
        model = ProductCategory
        fields = [
            'id', 'title'
        ]