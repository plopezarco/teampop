from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
import json
# Create your models here.

class Bezeroa(models.Model):
    helbidea = models.CharField(max_length=50)
    irudia = models.TextField()
    id_user= models.ForeignKey(User, on_delete=models.CASCADE)

class Produktua(models.Model):
    izena = models.CharField(max_length=50)
    prezioa = models.FloatField()
    irudia = models.TextField()
    kategoria = models.TextField()

class Ticket(models.Model):
    id_bezeroa = models.ForeignKey(Bezeroa,
        on_delete=models.CASCADE)
    data = models.DateTimeField()
    totala = models.FloatField()

class Ticket_Lerroa(models.Model):
    id_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    id_produktua = models.ForeignKey(Produktua, on_delete=models.CASCADE)
    kantitatea = models.FloatField()
    subtotala = models.FloatField()

class Mezua(models.Model):
    izena = models.CharField(max_length=50)
    email = models.EmailField()
    mezua = models.TextField()
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)