from django.urls import path

from .api_views import *


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('shops/', ShopListAPIView.as_view(), name='shop'),
]