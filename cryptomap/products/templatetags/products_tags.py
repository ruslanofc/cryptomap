from django import template

from products.models import ProductCategory

register = template.Library()


@register.simple_tag()
def get_products_categories():
    return ProductCategory.objects.all()