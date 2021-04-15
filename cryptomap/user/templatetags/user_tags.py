from django import template

from user.models import *

register = template.Library()


@register.simple_tag(takes_context=True)
def get_total_products(context):
    request = context['request']
    customer = CustomUser.objects.get(username=request.user.username)
    trackedItems = UserTrackedItems.objects.get(owner=customer)

    return trackedItems.total_products