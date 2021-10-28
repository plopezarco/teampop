from django.db import models
from django.db.models.base import Model

# Create your models here.

class Banatzailea(models.Model):
    nan = models.CharField(max_length=9)
    izena = models.CharField(max_length=50)
    abizena = models.CharField(max_length=50)
    email= models.EmailField()
    telefonoa = models.CharField(max_length=9)
    libre_dago = models.BooleanField()

class Bezeroa(models.Model):
    izena = models.CharField(max_length=50)
    abizena = models.CharField(max_length=50)
    email = models.EmailField()
    telefonoa = models.CharField(max_length=9)
    erabiltzailea = models.CharField(max_length=50)
    pasahitza = models.CharField(max_length=50)

class Produktua(models.Model):
    izena = models.CharField(max_length=50)
    prezioa = models.FloatField()
    irudia = models.TextField()
    kategoria = models.TextField()

class Ticket(models.Model):
    id_ticket = models.CharField(max_length=50)
    id_bezeroa = models.ForeignKey(Bezeroa,
        on_delete=models.CASCADE)
    id_banatzailea = models.ForeignKey(Banatzailea,
        on_delete=models.CASCADE)
    data = models.DateField()
    totala = models.FloatField()

class Ticket_Lerroa(models.Model):
    id_ticket = models.ForeignKey(Ticket,
        on_delete=models.CASCADE)
    id_produktua = models.ForeignKey(Produktua,
        on_delete=models.CASCADE)
    kantitatea = models.FloatField()
    subtotala = models.FloatField()