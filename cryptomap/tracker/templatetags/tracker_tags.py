from django import template
from tracker.bitcoin import get_btc_price


register = template.Library()


@register.simple_tag()
def multiply(priority, functional, *args, **kwargs):
    return priority * functional


def ask(b, c):
    a = get_btc_price()
    if b*a < c:
        return True
    else:
        return False


register.filter('ask', ask)


@register.simple_tag()
def get_price_btc():
    return get_btc_price()