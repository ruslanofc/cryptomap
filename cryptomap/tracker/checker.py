import decimal
import time
from .models import *
from .views import *
from .bitcoin import get_btc_price
from celery import shared_task
import random


@shared_task()
def track_for_discount():
    tp = TrackedProduct.objects.all()
    for product in tp:
        if product.requested_price < product.beginning_price_btc * decimal.Decimal(get_btc_price()):
            print(f'Discount for {product.product.title}')
            product_discount = TrackedProduct.objects.get(id=product.id)
            product_discount.discount_price = product.beginning_price_btc * decimal.Decimal(get_btc_price())
            product_discount.save()
            tracker = UserTracker.objects.get(products=product_discount.id)
            tracker.save()




while True:
    track_for_discount()
    time.sleep(15000000000)