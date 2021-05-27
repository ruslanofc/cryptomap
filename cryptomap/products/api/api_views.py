from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from .serializers import ProductsCategorySerializer
from ..models import ProductCategory


class ProductsCategoryListCreateAPIView(ListCreateAPIView):

    serializer_class = ProductsCategorySerializer
    queryset = ProductCategory.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']