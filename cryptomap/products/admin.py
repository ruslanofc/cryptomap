from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'shop', 'price_rub', 'price_btc')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ('product', 'category')
    list_display_links = ('product', 'category')
    search_fields = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)
