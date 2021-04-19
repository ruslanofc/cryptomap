from django.shortcuts import render
from .models import *
from .bitcoin import get_btc_price


def view_tracker(request):
    user = CustomUser.objects.get(username=request.user.username)
    tracker = UserTracker.objects.get(owner=user)
    btc_price = get_btc_price()

    return render(request, 'tracker/view_tracker.html', {"tracker": tracker, "btc_price": btc_price})
