""" posts views"""

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
# utilities
from datetime import datetime
import folium
import branca
from posts.models import NewProblem
import json


# ! Página principal
def main_menu(request):
    """[Provide the main page]
    Args:
        request
    """
    # return render(request, 'pagina.html', {'parametros': para usar en ese html})
    return render(request, 'index.html')

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

        
        try:
            # * Instanciamos el problema
            new_problem = NewProblem(latitud=Latitud, longitud=Longitud, tipo_problema=Problema,
            nivel_prioridad = Prioridad, ciudad=Ciudad, estado=Estado, codigo_postal=CP,
            informacion_extra=Informacion)

            # * Guardamos el problema en la base de datos
            new_problem.save()
            

            return render(request, 'registro.html',
            {'confirmation': 'Datos registrados exitosamente'})
        
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
    
    # * Añadir puntos al mapa
    #marcador1.add_to(maping)
    # * creamos el marcador
    #fire = folium.Marker(location=(19.702860, -101.190091), icon=folium.Icon(color="darkred", icon_color="#000", icon='fire-extinguisher', prefix='fa')) #! Morelia
    #sequia = folium.Marker(location=(19.513755, -101.708338), icon=folium.Icon(color="darkblue", icon_color="#000", icon='fa-tint', prefix='fa')) #! Pátzcuaro
    #deforestacion = folium.Marker(location=(19.513755, -107.608338), icon=folium.Icon(color="green", icon_color="#000", icon='fa-tree', prefix='fa')) #! Pátzcuaro
    #pesca = folium.Marker(location=(19.513755, -103.608338), icon=folium.Icon(color="darkblue", icon_color="#000", icon='fa-anchor', prefix='fa')) #! Pátzcuaro
    #estancamiento = folium.Marker(location=(19.513755, -106.608338), icon=folium.Icon(color="blue", icon_color="#000", icon='fa-chain-broken', prefix='fa')) #! Pátzcuaro
    #cambioSuelo = folium.Marker(location=(19.513755, -104.608338), icon=folium.Icon(color="white",icon_color='#000', icon='fa-refresh', prefix='fa')) #! Pátzcuaro
    #vertedero = folium.Marker(location=(19.513755, -111.608338), icon=folium.Icon(color="gray", icon_color="#000", icon='fa-trash', prefix='fa')) #! Pátzcuaro
    #toxico = folium.Marker(location=(19.513755, -108.608338), icon=folium.Icon(color="red", icon_color="#000", icon='fa-flask', prefix='fa')) #! Pátzcuaro
    #biologico = folium.Marker(location=(19.513755, -105.608338), icon=folium.Icon(color="red", icon_color="#000", icon='fa-warning', prefix='fa')) #! Pátzcuaro

    # * Hacemos un frame para el marcador
    #html = "<p>Problema: <strong>Deforestación</strong></p><p>Nivel de prioridad: <strong>Extremadamente alto</strong></p>"
    #iframe1 = branca.element.IFrame(html=html, width=256, height=128)
    #ejemplo = folium.Marker(location=(20.707637, -103.391825), popup=folium.Popup(iframe1, max_width=500), icon=folium.Icon(color="green", icon_color="#000", icon='fa-tree', prefix='fa'))
    
    
    ############ ! Creamos los objetos a partir de la filtración en la BD
    P_Incendio = NewProblem.objects.filter(tipo_problema='Incendio')
    P_Sequia = NewProblem.objects.filter(tipo_problema='Sequia')
    P_Deforestacion = NewProblem.objects.filter(tipo_problema='Deforestacion')
    P_Pesca_ilegal = NewProblem.objects.filter(tipo_problema='Pesca_ilegal')
    P_Estancamiento_agua = NewProblem.objects.filter(tipo_problema='Estancamiento_de_agua')
    P_Cambio_suelo = NewProblem.objects.filter(tipo_problema='Cambio_de_suelo')
    P_Vertederos_clandestinos = NewProblem.objects.filter(tipo_problema='Vertedero_clandestino')
    P_Desechos_toxicos = NewProblem.objects.filter(tipo_problema='Desechos_toxicos')
    P_Desechos_biologicos = NewProblem.objects.filter(tipo_problema='Desechos_biologicos')

    
    # P_Sequia[0].atribu # Obtener atributos
    # ! EXPLORAMOS LOS OBJETOS
    # * INCENDIO
    #print(P_Desechos_biologicos)
    #if P_Desechos_biologicos:
    #    print(P_Desechos_biologicos)
    
    if P_Incendio:
        for element in P_Incendio:  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=220, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="darkred", icon_color="#000", icon='fire-extinguisher', prefix='fa'))
            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_incendio)

    # * SEQUIA 
    if P_Sequia:
        for element in P_Sequia:  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=220, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="darkblue", icon_color="#000", icon='fa-tint', prefix='fa'))
            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_sequia)

    # * DEFORESTACION 
    if P_Deforestacion:
        for element in P_Deforestacion:  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=225, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="green", icon_color="#000", icon='fa-tree', prefix='fa'))
            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_deforestacion)

    # * PESCA ILEGAL
    if P_Pesca_ilegal:
        for element in P_Pesca_ilegal:  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=225, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="darkblue", icon_color="#000", icon='fa-anchor', prefix='fa'))
            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_pesca_ilegal)

    # * ESTANCAMIENTO DE AGUA
    if P_Estancamiento_agua:
        for element in P_Estancamiento_agua:  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=235, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="blue", icon_color="#000", icon='fa-chain-broken', prefix='fa'))

            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_estancamiento_agua)

    # * CAMBIO DE USO DE SUELO
    if P_Cambio_suelo:
        for element in P_Cambio_suelo:  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=230, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="white",icon_color='#000', icon='fa-refresh', prefix='fa'))

            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_cambio_de_suelo)
    
    # * VERTEDEROS CLANDESTINOS
    if P_Vertederos_clandestinos:
        for element in P_Vertederos_clandestinos:
            #print(element.estado)  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=235, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="gray", icon_color="#000", icon='fa-trash', prefix='fa'))

            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_vertederos_clandestinos)

    # * DESECHOS TOXICOS
    if P_Desechos_toxicos:
        for element in P_Desechos_toxicos:
            #print(element.estado)  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=230, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="red", icon_color="#000", icon='fa-flask', prefix='fa'))

            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_desechos_toxicos)

    # * DESECHOS BIOLOGICOS
    if P_Desechos_biologicos:
        for element in P_Desechos_biologicos:
            #print(element.estado)  
            html = f"<p>Problema: <strong>{element.tipo_problema}</strong></p>\
                <p>Nivel de prioridad: <strong>{element.nivel_prioridad}</strong></p>\
                <p>Fecha de registro: <strong>{element.created}</strong></p>\
                <p>Información extra: <strong>{element.informacion_extra}</strong></p>"
            iframe1 = branca.element.IFrame(html=html, width=230, height=200)
            the_element = folium.Marker(location=(element.latitud, element.longitud), popup=folium.Popup(iframe1, max_width=400), icon=folium.Icon(color="red", icon_color="#000", icon='fa-warning', prefix='fa'))
            
            # Añadimos el elemento a su grupo correspondiente
            the_element.add_to(grp_desechos_biologicos)
    
    ############ !
    


    #ejemplo.add_to(grp_deforestacion)
    
    # * Y ahora añadimos los grupos al mapa
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

def MyAPI(request):
    """ Where we can show the databases"""
    mydata = NewProblem.objects.all()
    data = {}
    idr = 1
    for element in mydata:
        registro = { 'Latitud': element.latitud, 'Longitud': element.longitud,
        'Tipo De Problema': element.tipo_problema, 'Prioridad': element.nivel_prioridad,
        'Ciudad': element.ciudad, 'Estado': element.estado, 
        'CP': element.codigo_postal, 'Información Extra': element.informacion_extra,
        'Fecha De Creación': str(element.created)}
        data[idr] = registro

        idr += 1
    
    return HttpResponse(json.dumps(data, ensure_ascii=False).encode('utf8'), content_type='application/json')


