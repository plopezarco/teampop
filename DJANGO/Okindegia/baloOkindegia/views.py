from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.models import User

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
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('erabiltzailea')
        password = request.POST.get('pasahitza')
        if User.objects.filter(username = username).exists() or User.objects.filter(email=email).exists():
            return JsonResponse({},status=409)
        else:
            user = User.objects.create_user(username = username, password = password, email = email)
            user.save()
            login(request,user)
            return JsonResponse({},status=200)
    return JsonResponse({},status=400)


def user_login(request):
    username = request.POST.get('erabiltzailea')
    password = request.POST.get('pasahitza')

    user= authenticate(request,username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({},status=200)
    else:
        return JsonResponse({},status=401)

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
