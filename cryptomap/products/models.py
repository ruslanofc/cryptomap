from django.db import models
from shops.models import *
from django.urls import reverse


class ProductCategory(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    price_rub = models.DecimalField(max_digits=20, decimal_places=7)
    price_btc = models.DecimalField(max_digits=20, decimal_places=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('view_product', kwargs={'product_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукта'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']


class ProductDescription(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Описание продукта'
        verbose_name_plural = 'Описание продуктов'