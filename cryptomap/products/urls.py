from django.urls import path

from .views import *

urlpatterns = [
    path('products/<int:product_id>/', view_product, name='view_product'),
    path('products/category/<int:category_id>/', get_products_by_category, name='products_by_category'),
]