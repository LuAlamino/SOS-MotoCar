import uuid

from django.db import models
from django.db.models import AutoField


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    factory_year = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    model_year = models.IntegerField(blank=True, null=True)
    Plate = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='carros/Fotos/', blank=True, null=True)
    value = models.FloatField()

# definição padrão para nao ficar mostrando car 'object'
    def __str__(self):
        return self.model