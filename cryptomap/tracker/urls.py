from django.urls import path

from .views import *

urlpatterns = [
    path('tracker/', view_tracker, name='view_tracker'),
    path('add_to_tracker/<int:product_id>/', AddToTrackerView.as_view(), name='add_to_tracker'),
    path('tracker/delete/',  DeleteItem.as_view(), name='delete_tracker_item'),
]