from django.urls import path
from .views import *


urlpatterns = [
    path('map', map, name="map"),
]