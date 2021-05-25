from django.urls import path

from .views import *

urlpatterns = [
    path('', AllShopsView.as_view(), name='home'),
    path('category/<int:category_id>/', ShopByCategory.as_view(), name='shops_by_category'),
    path('shop/<int:shops_id>/', ViewShop.as_view(), name='view_shops'),
    path('filter/', FilterCityShopView.as_view(), name='filter'),
    path('shops/search/', search, name='search'),
    path('shops/add_shops/', add_shops, name='add_shops'),
    path('shops/view_users_shops/', view_users_shops, name='view_users_shops'),
    path('shops/add_shops_descriptions/', add_shops_descriptions, name='add_shops_descriptions'),
]