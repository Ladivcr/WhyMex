"""
File for request control 
"""
# Django
from django.http import HttpResponse
# utilities 
from datetime import datetime 
import json

def hello_world(request):
    """Function to first hello world
    Args:
        request ([HttpResponse]): [Like a url]
    Returns:
        [HTML page]: [A page with the url]
    """ 
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')

    return HttpResponse(f'Hello from whymex! Current time: {now}')

def sort_integers(request):
    """return a json response with sorted integers
    Args:
        request ([HttpResponse]): [/?numbers=1,2,33,2,1]
    Returns:
        [HTML page]: [numbers in json ]
    """

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    """return a json response with sorted integers
    Args:
        request ([HttpResponse]): [/?numbers=1,2,33,2,1]
        name ([str]): ['Franklin']
        age ([int]): [33]
    Returns:
        [HTML page]: [numbers in json ]
    """

    if age < 12: 
        message = f'Sorry {name}, you are not allowed here'
    else: 
        message = f'Hi {name}! Welcome to platzigram'
    
    return HttpResponse(message)
