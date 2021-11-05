from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .models import Produktua

# Create your views here.

def produktuak(request):
    produktuak_list = Produktua.objects.all()
    kategoriak = []
    for p in produktuak_list:
        if p.kategoria not in kategoriak:
            kategoriak.append(p.kategoria)
    dicc = {'produktuak' : produktuak_list, 'kategoriak' : kategoriak}
    return render(request, "produktuak.html", dicc)

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            erabiltzailea = form.cleaned_data.get('erabiltzailea')
            pasahitza = form.cleaned_data.get('pasahitza') 
            pasahitza2 = form.cleaned_data.get('pasahitza2') 
            email = form.cleaned_data.get('email') 
            if pasahitza == pasahitza2:
                pasahitza = make_password('BALO@1234')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method=="POST":
        username=request.POST["erabiltzailea-login"]
        password=request.POST["pasahitza-login"]

        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request,'Erabiltzaile edo Pasahitza okerrak')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def erosi(request):
    produktuak_list = request.POST.get('produktuakLista')
    dicc = {'produktuakLista' : produktuak_list}
    return render(request, "erosi.html", dicc)


def produktuakFiltratu(request):
    kategoria = request.POST.get('kategoria')
    if kategoria != 'guztiak':
        produktuak_list = Produktua.objects.filter(kategoria = kategoria)
    else:
        produktuak_list = Produktua.objects.all()
    return JsonResponse({'produktuak' : list(produktuak_list.values())}, status=200)