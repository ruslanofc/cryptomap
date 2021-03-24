from django.urls import path

from .views import *

urlpatterns = [
    path('products/<int:product_id>/', view_product, name='view_product'),
]