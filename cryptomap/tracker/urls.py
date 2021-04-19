from django.urls import path

from .views import *

urlpatterns = [
    path('tracker/', view_tracker, name='view_tracker'),
]