from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration_view, name='register'),
]

