import uuid

from django.db import models
from django.db.models import AutoField


class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CarInventory(models.Model):
    cars_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    cars_value = models.FloatField(default=0)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.cars_count} - {self.cars_value} '

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name='Cidades_Carros' , blank=True, null=True)
    factory_year = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    model_year = models.IntegerField(blank=True, null=True)
    Plate = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='carros/Fotos/', blank=True, null=True)
    value = models.FloatField()
    bio = models.TextField(blank=True, null=True)


# definição padrão para nao ficar mostrando car 'object'
    def __str__(self):
        return self.model