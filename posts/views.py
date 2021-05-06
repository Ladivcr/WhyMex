""" posts views"""

# Django
from django.shortcuts import render
#from django.http import HttpResponse
# utilities
from datetime import datetime
import folium 


now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': now,
        'photo': 'https://picsum.photos/200/200/?image=1036',
         
    },
    {
        'title': 'Via lactea',
        'user': {
            'name': 'C. vander',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': now,
        'photo': 'https://picsum.photos/200/200/?image=903',
         
    },
]

# ESto es lo que estoy viendo
# ! Página principal
def main_menu(request): 
    """[Provide the main page]
    Args: 
        request
    """
    # return render(request, 'pagina.html', {'parametros': para usar en ese html})
    return render(request, 'index.html', {'posts': posts})

# ! Página para registrar problemas
def register_problem(request): 
    """[Provide the page where the user can register new problems]
    Args:
        request
    """
    return render(request, 'registro.html')

# ! Página para ver los problemas en un mapa
def show_map(request): 
    """[Provide the page where the user can watch the different problems]
    Args:
        request
    """ 
    #creation of map comes here + business logic
    # * where the map start: Mexico
    maping = folium.Map(location=(22.9998589, -100.9994856), zoom_start=5)

    #test = folium.Html('<b>Hello world</b>', script=True)
    #popup = folium.Popup(test, max_width=2048)
    #folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(maping)
    
    
    # * Añadir puntos al mapa
    #marcador1.add_to(maping)
    # * creamos el marcador
    Morelia = folium.Marker(location=(19.702860, -101.190091), icon=folium.Icon(color="red", icon='info-sign')) #! Morelia
    Patzcuaro = folium.Marker(location=(19.513755, -101.608338), icon=folium.Icon(color="blue", icon='cloud')) #! Pátzcuaro
    
    # * Creamos grupos para los marcadores
    grp_Mor = folium.FeatureGroup(name='Pertenece a Morelia')
    grp_Pat = folium.FeatureGroup(name='Pertenece a Pátzcuaro')
    
    # Añadimos los marcadores AL GRUPO AL QUE CORRESPONDAN (NO AL MAPA)
    Morelia.add_to(grp_Mor)
    Patzcuaro.add_to(grp_Pat)
    # Y ahora añadimos los grupos al mapa
    grp_Mor.add_to(maping)
    grp_Pat.add_to(maping)
    # Y añadimos, además, el control de capas
    folium.LayerControl().add_to(maping)

    maping=maping._repr_html_() # * updated, with this I can see the map
    context = {'my_map': maping}
    return render(request, 'mapa.html', context)

# ! Página para contactar con el proyecto
def contact(request): 
    """[Provide the page where the user can contact to me]
    Args:
        request
    """
    return render(request, 'contacto.html')
