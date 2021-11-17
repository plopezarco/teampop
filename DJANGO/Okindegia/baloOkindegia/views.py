from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required,user_passes_test
import json
from .models import Bezeroa, Mezua, Produktua, Ticket, Ticket_Lerroa

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
            bezeroa = Bezeroa.objects.create(id_user = user, email = user.email)
            bezeroa.save()
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

def check_login(request):
    if request.user.is_authenticated:
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=401)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/index")

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

def mezuaGorde(request):
    izena = request.POST.get('izena')
    email = request.POST.get('email')
    mezua = request.POST.get('mezua')

    mezuaObj = Mezua.objects.create(izena = izena, email = email, mezua = mezua)
    return JsonResponse({'mezua': mezuaObj.toJSON()}, status=200)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def mezua(request):
    mezuakList = Mezua.objects.all()
    dicc = {'mezuak' : mezuakList}
    return render(request, "mezuak.html", dicc)

@login_required
def ordaindu(request):
    produktuak = request.POST.get('produktuak')
    totala = request.POST.get('totala')

    try:    
        bezeroa = Bezeroa.objects.filter(id_user = request.user.id).first()
        fecha = timezone.now().isoformat()
        ticket = Ticket.objects.create(data = fecha, totala = totala, id_bezeroa = bezeroa)
        ticket.save()

        prodjson = json.loads(produktuak)
        for p in prodjson:
            subtotala = float(p["kopurua"]) * float(p["prezioa"])
            produktua = Produktua.objects.filter(id = p["id"]).first()
            lerroa = Ticket_Lerroa.objects.create(kantitatea = p["kopurua"], subtotala = subtotala, id_produktua = produktua, id_ticket = ticket)
            lerroa.save()
        return JsonResponse({}, status=200)
    except:
        return JsonResponse({}, status=500)

@login_required
def profila(request):
    user = request.user
    bezeroa = Bezeroa.objects.filter(id_user = user).first()
    ticketak = Ticket.objects.filter(id_bezeroa = bezeroa).all()

    for t in ticketak:
        lerroak = Ticket_Lerroa.objects.filter(id_ticket = t).select_related('id_produktua')
        print(lerroak.first().id_produktua)
        t.lerroak = lerroak

    dicc = {'user' : request.user, 'bezeroa' : bezeroa, 'eskaerak' : ticketak}
    return render(request, "profile.html", dicc)