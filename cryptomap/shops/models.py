from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория магазина'
        verbose_name_plural = 'Категории магазинов'


class Shop(models.Model):
    title = models.CharField(max_length=150)
    city = models.CharField(max_length=60, default="Kazan")
    address = models.CharField(max_length=300)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['created_at']


class ShopDescription(models.Model):
    shop = models.OneToOneField(
        Shop,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    email = models.EmailField(max_length=300, blank=True, unique=True)
    url = models.URLField(max_length=300, blank=True)
    telegram_url = models.URLField(max_length=300, blank=True)
    pay_in_rub = models.BooleanField(default=True)
    pay_in_btc = models.BooleanField(default=True)

    def __str__(self):
        return self.shop.title

    class Meta:
        verbose_name = 'Описание магазина'
        verbose_name_plural = 'Описание магазинов'
