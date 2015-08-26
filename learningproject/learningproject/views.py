__author__ = 'marcelo'
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World')
