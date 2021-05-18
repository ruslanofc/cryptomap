from django.urls import path

from .api_views import *


urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/delete', CategoryDeleteAPIView.as_view(), name='categories_delete'),
    path('categories/<int:pk>/update', CategoryUpdateAPIView.as_view(), name='categories_update'),
    path('shops/', ShopListAPIView.as_view(), name='shops'),
    path('shops/<str:id>/', ShopDetailAPIView.as_view(), name='shop_detail'),
]