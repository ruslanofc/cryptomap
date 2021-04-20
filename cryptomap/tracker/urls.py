from django.urls import path

from .views import *

urlpatterns = [
    path('tracker/', view_tracker, name='view_tracker'),
    path('add_to_tracker/<int:product_id>/', AddToTrackerView.as_view(), name='add_to_tracker'),
]