from django.shortcuts import render
from django.conf import settings
from shops.models import Shop


def map(request):
	shops = Shop.objects.all()
	array_of_array = []
	for item in shops:
		array_of_array.append([float(item.latitude), float(item.longitude), (item.id), (item.title)])
	context = {"google_api_key": settings.GOOGLE_API_KEY, 'shops': shops, 'marker': array_of_array}
	return render(request, 'map/map.html', context)

