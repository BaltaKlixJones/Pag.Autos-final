from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autos(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return self.marca +" "+ self.modelo

class Motos(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return self.marca +" "+ self.modelo


class Camiones(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return self.marca +" "+ self.modelo


class Aviones(models.Model):
    modelo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return self.modelo +" " + self.color


class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null= True, blank= True)

