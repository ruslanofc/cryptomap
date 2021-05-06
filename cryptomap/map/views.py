from django.shortcuts import render
from django.conf import settings


def map(request):
	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'map/map.html', context)

