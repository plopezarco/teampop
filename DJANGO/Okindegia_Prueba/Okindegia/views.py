import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Produktua(object):
    
    def __init__(self, izena, prezioa):
        self.izena = izena
        self.prezioa = prezioa


def saludo(request):
    p1 = Persona("Naruto", "Uzumaki")
    fecha_actual = datetime.datetime.now()
    animes= ["Naruto", "One Piece", "Jujutsu Kaisen", "Kimetsu no Yaiba", "Attack on Titan"]
    dicc = {"persona": p1, "ahora": fecha_actual, "animes": animes}

    return render(request, "index.html", dicc)


def despedida(request):
    return HttpResponse("Adios mundo")


def getDate(request):
    fecha_actual = datetime.datetime.now()
    doc = """<html>
    <body>
    <h5>
    Fecha y hora actuales: %s
    <h5>
    <body>
    <html>""" % fecha_actual

    return HttpResponse(doc)


def calculaEdad(request, edad, ano):
    periodo = ano - 2021
    edadFutura = edad + periodo
    doc = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>" % (ano, edadFutura)

    return HttpResponse(doc)


def produktuak(request):
    produktuList = [Produktua("Ogi handia", 2.3),Produktua("Napolitana", 0.7),Produktua("Kroisant", 1)]
    animes= ["Naruto", "One Piece", "Jujutsu Kaisen", "Kimetsu no Yaiba", "Attack on Titan"]
    dicc2 = {"produktuak" : produktuList, "animes" : animes, "p1" : Produktua("Ogi handia", 2.3)}
    
    return render(request, "produktuak.html", dicc2)
