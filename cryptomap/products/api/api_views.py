from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductsCategorySerializer
from ..models import ProductCategory


class ProductsCategoryList(APIView):
    def get(self, request, format=None):
        categories = ProductCategory.objects.all()
        serializer = ProductsCategorySerializer(categories, many=True)
        return Response(serializer.data)
