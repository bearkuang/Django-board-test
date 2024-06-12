from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .services import my_service_function

def index(request):
    data = my_service_function()
    return render(request, 'myapp/index.html', {'data': data})

def simple_view(request):
    return HttpResponse("Hello, world!")