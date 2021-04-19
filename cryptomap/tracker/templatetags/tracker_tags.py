from django import template
from tracker.bitcoin import get_btc_price


register = template.Library()


@register.simple_tag()
def multiply(priority, functional, *args, **kwargs):
    return priority * functional


@register.simple_tag()
def get_price_btc():
    return get_btc_price()