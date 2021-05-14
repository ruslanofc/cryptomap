import decimal
import time
from .models import *
from .views import *
from .bitcoin import get_btc_price
from celery import shared_task
import random
from django.core.mail import send_mail


@shared_task(name="track_for_discount")
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

            send_mail(f'Discount for {product_discount.product.title}',
                             f'Now price is {product_discount.discount_price} old price is {product_discount.beginning_price_rub}',
                             'cryptomap2021@gmail.com',
                             [f'{product_discount.owner.email}'], fail_silently=False)


while True:
    track_for_discount()
    time.sleep(3600)