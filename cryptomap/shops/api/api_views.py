from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .serializers import CategorySerializer, ShopSerializer
from ..models import Category, Shop, CustomUser


class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']


class ShopListAPIView(ListAPIView):

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['owner__id', 'city']