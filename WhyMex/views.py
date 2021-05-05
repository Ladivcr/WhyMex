"""
File for request control 
"""
# Django
from django.http import HttpResponse
# utilities 
from datetime import datetime 
import json

# ! MAPA
from django.views.generic.base import TemplateView
#import geopandas as gpd

# ? SIENDO FRANCOS CREO QUE ESTO NO ES NECESARIO PUES YA BORRE MAP.HTML
class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"

# ! TERMINA MAPA

def hello_world(request):
    """Function to first hello world
    Args:
        request ([HttpResponse]): [Like a url]
    Returns:
        [HTML page]: [A page with the url]
    """ 
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')

    return HttpResponse(f'Hello from whymex! Current time: {now}')