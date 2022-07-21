from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HTTPResponse('Hello Word!')

def teste(request):
    return HTTPResponse('Minha pagina de teste')