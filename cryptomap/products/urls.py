from django.urls import path

from .views import *

urlpatterns = [
    path('products/<int:product_id>/', view_product, name='view_product'),
    path('products/all/', ProductsView.as_view(), name='all_products'),
    # path('products/category/<int:category_id>/', get_products_by_category, name='products_by_category'),
    path('products/category/<int:category_id>/', ProductsByCategory.as_view(), name='products_by_category'),
    path('products/add_product/<int:shop_id>/', add_product, name='add_product'),
    path('products/add_product_description/', add_product_description, name='add_product_description'),
]