from django.urls import path

from .api_views import *


urlpatterns = [
    path('products/categories/', ProductsCategoryListCreateAPIView.as_view(), name='productsCategories'),
]