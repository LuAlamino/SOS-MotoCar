from django.contrib import admin

from carros.models import Car, Brand, Cidade
from Mecanico.models import Mecanico



class CarAdmin(admin.ModelAdmin):
    list_display = ('model','cidade' , 'factory_year', 'brand', 'model_year', 'value', 'Plate')
    search_fields = ('model', 'brand', 'Plate', 'cidade') # Aqui eu coloco em qual campo ele vai fazer a busca

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', )
    search_fields = ('nome', )

#tem que colocar igual abaixo para aparecer no admin
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Cidade, CidadeAdmin)



class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('name', 'cidade', 'bairro', 'name_fantasy', 'carros_Trabalha',)
    search_fields = ('name','name_fantasy','cidade' , 'bairro')

admin.site.register(Mecanico, MecanicoAdmin)