""" posts views"""

# Django
from django.shortcuts import render
#from django.http import HttpResponse
# utilities
from datetime import datetime


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
def main_menu(request): 
    """[Provide the main page]
    Args: 
        request
    """
    # return render(request, 'pagina.html', {'parametros': para usar en ese html})
    return render(request, 'index.html', {'posts': posts})

def register_problem(request): 
    """[Provide the page where the user can register new problems]
    Args:
        request
    """
    return render(request, 'registro.html')

def map(request): 
    """[Provide the page where the user can watch the different problems]
    Args:
        request
    """
    return render(request, 'mapa.html')

def contact(request): 
    """[Provide the page where the user can contact to me]
    Args:
        request
    """
    return render(request, 'contacto.html')
