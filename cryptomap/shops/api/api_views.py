from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from .serializers import CategorySerializer, ShopSerializer, ShopDescriptionSerializer
from ..models import Category, Shop, CustomUser, ShopDescription


# посмотреть все категории магазинов либо создать новую категорию
class CategoryListCreateAPIView(ListCreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']


# посмотреть одну конкретную категорию
class CategoryDetailAPIView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'


# обновить категорию магазинов
class CategoryUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# удалить категорию магазинов
class CategoryDeleteAPIView(DestroyAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# посмотреть все магазины
class ShopListCreateAPIView(ListCreateAPIView):

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['owner__id', 'city']


# псомтреть конкретный магазин
class ShopDetailAPIView(RetrieveAPIView):

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    lookup_field = 'id'


# посмотреть описание конкретного магазина
class ShopDescriptionDetailAPIView(RetrieveAPIView):

    serializer_class = ShopDescriptionSerializer
    queryset = ShopDescription.objects.all()
    lookup_field = 'shop_id'