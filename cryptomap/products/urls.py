from django.urls import path

from .views import *

urlpatterns = [
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='view_product'),
    path('products/all/', ProductsView.as_view(), name='all_products'),
    path('products/category/<int:category_id>/', ProductsByCategory.as_view(), name='products_by_category'),
    path('products/add_product/<int:shop_id>/', add_product, name='add_product'),
    path('products/add_product_description/', add_product_description, name='add_product_description'),
]