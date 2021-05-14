from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .bitcoin import get_btc_price
from django.views.generic import DetailView, View
from django.db.models import F
from django.contrib import messages
from .lstm import get_predict
from .forms import *


def view_tracker(request):
    user = CustomUser.objects.get(username=request.user.username)
    tracker, created = UserTracker.objects.get_or_create(owner=user)
    price_btc = get_btc_price()

    return render(request, 'tracker/view_tracker.html', {"tracker": tracker, "price_btc": price_btc})


def prediction(request, coin):
    prediction, image = get_predict(coin)
    print(type(prediction))

    return render(request, 'tracker/prediction.html', {"prediction": prediction, "image": image, "coin": coin})


def add_coin_to_predict(request):
    if request.method == 'POST':
        coin = request.POST['coin']
        return redirect('prediction', coin=coin)
    else:
        return render(request, 'tracker/add_coin_to_predict.html')


class AddToTrackerView(View):
    def get(self, request, product_id, *args, **kwargs):
        user = CustomUser.objects.get(username=request.user.username)
        tracker, created = UserTracker.objects.get_or_create(owner=user)
        product = Product.objects.get(pk=product_id)
        tp, created = TrackedProduct.objects.get_or_create(owner=user, product=product, requested_price=5, tracker=tracker, beginning_price_rub=product.price_rub, beginning_price_btc=product.price_btc, discount_price='No Discount')
        if created:
            tracker.products.add(tp)
            tracker.total_products = F('total_products')+1
            messages.add_message(request, messages.INFO, "Товар успешно добавлен")
            tracker.save()
        else:
            messages.add_message(request, messages.INFO, "Товар уже отслеживается")
        return redirect('view_tracker')


class UpdateCrud(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        percent = request.GET.get('percent', None)

        obj = TrackedProduct.objects.get(id=id1)
        obj.price_change = percent

        obj.save()

        user = {'price_change': obj.price_change}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteItem(View):
    def get(self, request):
        user = CustomUser.objects.get(username=request.user.username)

        id1 = request.GET.get('id', None)

        tracker = UserTracker.objects.get(owner=user)
        tracker.total_products = F('total_products') - 1
        tracker.save()
        TrackedProduct.objects.get(id=id1).delete()

        data = {
            'deleted': True,
            # 'count': a
        }
        return JsonResponse(data)