from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from .serializers import CategorySerializer, ShopSerializer
from ..models import Category, Shop, CustomUser


class CategoryListCreateAPIView(ListCreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']


class CategoryUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDeleteAPIView(DestroyAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ShopListAPIView(ListAPIView):

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['owner__id', 'city']


class ShopDetailAPIView(RetrieveAPIView):

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    lookup_field = 'id'
