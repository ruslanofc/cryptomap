from django.shortcuts import render
from .models import *


def view_tracker(request):
    user = CustomUser.objects.get(username=request.user.username)
    tracker = UserTracker.objects.get(owner=user)

    return render(request, 'tracker/view_tracker.html', {"tracker": tracker})
