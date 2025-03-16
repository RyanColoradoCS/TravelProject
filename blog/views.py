from django.shortcuts import render
from django.views.generic import ListView, DetailView, View # A generic class-based view that displays a list of objects.
from .models import Post, GoogleMapsData, Locations
from django.conf import settings
import logging
import requests

logger = logging.getLogger(__name__)


# Create your views here.
# this is class based view instead of funtion based view

class BlogListView(ListView):
    model = Post # Specifies the model to use. In this case, Post is the model whose objects will be listed.
    template_name = "blog.html" 
    # template_name = "home.html"  Specifies the template to use for rendering the list. 
    # In this case, home.html is the template file where the list of posts will be displayed.

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

def retrieve_data_from_google_maps():
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={settings.GOOGLE_MAPS_API_KEY}'
    logger.info(f"Requesting URL: {url}")
    response = requests.get(url)
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")
    
    if response.status_code == 200:
        api_data = response.json()
        if api_data.get('results'):
            return api_data['results'][0]['geometry']['location']
        else:
            logger.error(f"No results found in API response: {api_data}")
            return None
    else:
        logger.error(f"Failed to retrieve data. Status Code: {response.status_code}")
        return None

def store_api_data(request):
    api_data = retrieve_data_from_google_maps()
    if api_data:
        obj = GoogleMapsData(location_name='Sydney Opera House', latitude=api_data['lat'], longitude=api_data['lng'])
        obj.save()
        logger.info("Data saved successfully.")
        return render(request, 'store_data.html', {'success': 'Data saved successfully'})
    else:
        logger.error("Failed to retrieve data from Google Maps API.")
        return render(request, 'blog/store_data.html', {'error': 'Failed to retrieve data'})

class HomeView(ListView):
    model = Locations
    template_name = "mydata.html"
    context_object_name = 'locations'
    # form_class = 
    # success_url = "/"
    
    
class GeoCodingView(View):
    # model = 
    template_name = "geocoding.html"
    
    def get(self, request, pk):
        
        location = Locations.objects.get(pk=pk)
        
        context = {
            'location':location
        }

        return render(request, self.template_name, context)