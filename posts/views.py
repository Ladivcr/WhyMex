""" posts views"""

# Django
from django.shortcuts import render, redirect
#from django.http import HttpResponse
# utilities
from datetime import datetime
import folium
import branca
from posts.models import NewProblem

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
    #import pdb; pdb.set_trace()
    if request.method == 'POST': 
        Latitud = request.POST['latitud'] # * No vacio
        Longitud = request.POST['longitud'] # * No vacio
        Problema = request.POST['problema'] # * No vacio
        Prioridad = request.POST['prioridad'] # * No vacio
        Estado = request.POST['estado'] # * No vacio
        try:
            Ciudad = request.POST['ciudad'] # ! Si vacio
        except: Ciudad = "Null"
        try:
            CP = request.POST['CP'] # ! Si vacio
        except: CP = "Null"
        try:
            Informacion = request.POST['about'] # ! Si vacio
        except: Informacion = "Null"

        print("Datos recibidos:")
        print(Latitud, Longitud, Problema, Prioridad, Ciudad, Estado, CP, Informacion)
        
        try:
            new_problem = NewProblem(latitud=Latitud, longitud=Longitud, tipo_problema=Problema,
            nivel_prioridad = Prioridad, ciudad=Ciudad, estado=Estado, codigo_postal=CP,
            informacion_extra=Informacion)
            print(new_problem)

            new_problem.save()

        
        except:
            return render(request, 'registro.html',
            {'error': 'No hemos podido registrar el problema\nIntenta de nuevo'})
        
        #print(latitud, longitud, problema, prioridad, ciudad, estado, codigo_postal, mas_informacion)
        # si ya se registraron en la bd
        return redirect('mostrar_mapa')


    
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



    # * Añadir puntos al mapa
    #marcador1.add_to(maping)
    # * creamos el marcador
    fire = folium.Marker(location=(19.702860, -101.190091), icon=folium.Icon(color="darkred", icon_color="#000", icon='fire-extinguisher', prefix='fa')) #! Morelia
    sequia = folium.Marker(location=(19.513755, -101.708338), icon=folium.Icon(color="darkblue", icon_color="#000", icon='fa-tint', prefix='fa')) #! Pátzcuaro
    deforestacion = folium.Marker(location=(19.513755, -107.608338), icon=folium.Icon(color="green", icon_color="#000", icon='fa-tree', prefix='fa')) #! Pátzcuaro
    pesca = folium.Marker(location=(19.513755, -103.608338), icon=folium.Icon(color="darkblue", icon_color="#000", icon='fa-anchor', prefix='fa')) #! Pátzcuaro
    estancamiento = folium.Marker(location=(19.513755, -106.608338), icon=folium.Icon(color="blue", icon_color="#000", icon='fa-chain-broken', prefix='fa')) #! Pátzcuaro
    cambioSuelo = folium.Marker(location=(19.513755, -104.608338), icon=folium.Icon(color="white",icon_color='#000', icon='fa-refresh', prefix='fa')) #! Pátzcuaro
    vertedero = folium.Marker(location=(19.513755, -111.608338), icon=folium.Icon(color="gray", icon_color="#000", icon='fa-trash', prefix='fa')) #! Pátzcuaro
    toxico = folium.Marker(location=(19.513755, -108.608338), icon=folium.Icon(color="red", icon_color="#000", icon='fa-flask', prefix='fa')) #! Pátzcuaro
    biologico = folium.Marker(location=(19.513755, -105.608338), icon=folium.Icon(color="red", icon_color="#000", icon='fa-warning', prefix='fa')) #! Pátzcuaro

    # *La información solo será la posición del marcador
    # * os dejo a vosotros la innovación
    html = "<p>Problema: <strong>Deforestación</strong></p><p>Nivel de importancia: <strong>Extremadamente alto</strong></p>"
    iframe1 = branca.element.IFrame(html=html, width=256, height=128)
    ejemplo = folium.Marker(location=(20.707637, -103.391825), popup=folium.Popup(iframe1, max_width=500), icon=folium.Icon(color="green", icon_color="#000", icon='fa-tree', prefix='fa'))
    # * Creamos grupos para los marcadores
    grp_incendio = folium.FeatureGroup(name='Incendio')
    grp_sequia = folium.FeatureGroup(name="Sequia")
    grp_deforestacion = folium.FeatureGroup(name="Deforestación")

    grp_pesca_ilegal = folium.FeatureGroup(name="Pesca ilegal")
    grp_estancamiento_agua = folium.FeatureGroup(name="Estancamiento de agua")
    grp_cambio_de_suelo = folium.FeatureGroup(name="Cambio de uso de suelo")
    grp_vertederos_clandestinos = folium.FeatureGroup(name="Vertederos clandestinos")
    grp_desechos_toxicos = folium.FeatureGroup(name="Desechos tóxicos tirados clandestinamente")
    grp_desechos_biologicos = folium.FeatureGroup(name="Desechos biológicos tirados clandestinamente")


    ejemplo.add_to(grp_deforestacion)
    # Añadimos los marcadores AL GRUPO AL QUE CORRESPONDAN (NO AL MAPA)
    fire.add_to(grp_incendio)
    sequia.add_to(grp_sequia)
    deforestacion.add_to(grp_deforestacion)
    pesca.add_to(grp_pesca_ilegal)
    estancamiento.add_to(grp_estancamiento_agua)
    cambioSuelo.add_to(grp_cambio_de_suelo)
    vertedero.add_to(grp_vertederos_clandestinos)
    toxico.add_to(grp_desechos_toxicos)
    biologico.add_to(grp_desechos_biologicos)
    # Y ahora añadimos los grupos al mapa
    grp_incendio.add_to(maping)
    grp_sequia.add_to(maping)
    grp_deforestacion.add_to(maping)
    grp_pesca_ilegal.add_to(maping)
    grp_estancamiento_agua.add_to(maping)
    grp_cambio_de_suelo.add_to(maping)
    grp_vertederos_clandestinos.add_to(maping)
    grp_desechos_toxicos.add_to(maping)
    grp_desechos_biologicos.add_to(maping)
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


# ! Página para ayudar al registro de datos
def help(request):
    """[Provide the page where the user can contact to me]
    Args:
        request
    """
    return render(request, 'ayuda.html')
