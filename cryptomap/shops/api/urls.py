from django.urls import path

from .api_views import *


urlpatterns = [
    # посмотреть все категории магазинов либо создать новую категорию
    path('shops/categories/', CategoryListCreateAPIView.as_view(), name='categories'),
    # посмотреть одну конкретную категорию
    path('shops/categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='shop_category'),
    # удалить категорию магазинов
    path('shops/categories/<int:pk>/delete', CategoryDeleteAPIView.as_view(), name='categories_delete'),
    # обновить категорию магазинов
    path('shops/categories/<int:pk>/update', CategoryUpdateAPIView.as_view(), name='categories_update'),
    # посмотреть все магазины
    path('shops/', ShopListCreateAPIView.as_view(), name='shops'),
    # псомтреть конкретный магазин
    path('shops/<str:id>/', ShopDetailAPIView.as_view(), name='shop_detail'),
    # посмотреть описание конкретного магазина
    path('shops/description/<str:shop_id>/', ShopDescriptionDetailAPIView.as_view(), name='shop_detail'),
]