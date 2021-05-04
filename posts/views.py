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
        {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Thespianartist',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': now,
        'photo': 'https://picsum.photos/200/200/?image=1076',
         
    },
    

]

def list_posts(request): 
    """ list existing posts """
    return render(request, 'index.html', {'posts': posts})