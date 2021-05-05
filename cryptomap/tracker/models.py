from django.db import models
from products.models import *
from user.models import *


class TrackedProduct(models.Model):
    requested_price = models.IntegerField(null=True, blank=True)
    discount_price = models.CharField(max_length=100)
    owner = models.ForeignKey('user.CustomUser', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    tracker = models.ForeignKey('UserTracker', verbose_name='UserTracker', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey('products.Product', blank=False, on_delete=models.CASCADE)
    beginning_price_rub = models.DecimalField(max_digits=20, decimal_places=7)
    beginning_price_btc = models.DecimalField(max_digits=20, decimal_places=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Продукт: {} (отслеживаемый)".format(self.product.title)


class UserTracker(models.Model):
    owner = models.ForeignKey('user.CustomUser', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(TrackedProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price_rub = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена в рублях')
    final_price_btc = models.DecimalField(max_digits=9, default=0, decimal_places=9, verbose_name='Общая цена в btc')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('view_tracker', kwargs={'tracker_id': self.pk})

