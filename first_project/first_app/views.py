from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")
def learn_django(request):
        return HttpResponse("Hello django")
def learn_python(request):
    return HttpResponse("Hello python")
