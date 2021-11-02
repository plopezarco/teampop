from django.shortcuts import render

from .models import Produktua

# Create your views here.

def produktuak(request):
    produktuak_list = Produktua.objects.all()
    dicc = {'produktuak' : produktuak_list}
    
    return render(request, "produktuak.html", dicc)

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")