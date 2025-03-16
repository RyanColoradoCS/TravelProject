# views.py
from django.shortcuts import render
from django.conf import settings

def map(request):
    context = {'key': settings.GOOGLE_MAPS_API_KEY}
    return render(request, 'map.html', context)
