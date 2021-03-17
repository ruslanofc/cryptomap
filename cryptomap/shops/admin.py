from django.contrib import admin
from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'address')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class ShopDescriptionAdmin(admin.ModelAdmin):
    list_display = ('shop', 'category', 'url')
    list_display_links = ('shop', 'category')
    search_fields = ('title', 'address')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ShopDescription, ShopDescriptionAdmin)

