from django.urls import path

from .views import *

urlpatterns = [
    path('products/<int:product_id>/', view_product, name='view_product'),
    path('products/category/<int:category_id>/', get_products_by_category, name='products_by_category'),
    path('products/add_product/<int:shop_id>/', add_product, name='add_product'),
    path('products/add_product_description/', add_product_description, name='add_product_description'),
]