from django.contrib import admin

from carros.models import Car, Brand
from Mecanico.models import Mecanico


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'factory_year', 'brand', 'model_year', 'value', 'Plate')
    search_fields = ('model', 'brand', 'Plate') # Aqui eu coloco em qual campo ele vai fazer a busca

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

#tem que colocar igual abaixo para aparecer no admin
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)


class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('name', 'bairro', 'name_fantasy', 'carros_Trabalha')
    search_fields = ('name','name_fantasy', 'bairro')

admin.site.register(Mecanico, MecanicoAdmin)