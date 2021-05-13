from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='shops_by_category'),
    path('shops/<int:shops_id>/', view_shops, name='view_shops'),
    path('shops/add_shops/', add_shops, name='add_shops'),
    path('shops/view_users_shops/', view_users_shops, name='view_users_shops'),
    path('shops/add_shops_descriptions/', add_shops_descriptions, name='add_shops_descriptions'),
]