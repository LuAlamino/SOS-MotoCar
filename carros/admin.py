from django.contrib import admin

from Mecanico.forms import MecanicoModelForm
from carros.forms import CarModelForm, cidadeModelForm
from carros.models import Car, Brand, Cidade
from Mecanico.models import Mecanico


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarModelForm
    list_display = [
        'get_model_display',
        'get_cidade_nome',
        'get_factory_year_display',
        'get_brand_name',
        'get_model_year_display',
        'get_value_display',
        'get_plate_display'
    ]
    search_fields = (
        'model',
        'brand__name',
        'Plate',
        'cidade__nome'
    )
    autocomplete_fields = ['brand', 'cidade']

    def get_model_display(self, obj):
        return obj.model
    get_model_display.short_description = 'Modelo'

    def get_cidade_nome(self, obj):
        return obj.cidade.nome if obj.cidade else '-'
    get_cidade_nome.short_description = 'Cidade'

    def get_factory_year_display(self, obj):
        return obj.factory_year
    get_factory_year_display.short_description = 'Ano Fabricação'

    def get_brand_name(self, obj):
        return obj.brand.name if obj.brand else '-'
    get_brand_name.short_description = 'Marca'

    def get_model_year_display(self, obj):
        return obj.model_year
    get_model_year_display.short_description = 'Ano de Modelo'

    def get_value_display(self, obj):
        return obj.value
    get_value_display.short_description = 'Valor'

    def get_plate_display(self, obj):
        return obj.Plate
    get_plate_display.short_description = 'Placa'

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    form = cidadeModelForm
    list_display = ('get_cidade_display', )
    search_fields = ('nome', )

    def get_cidade_display(self, obj):
        return obj.nome
    get_cidade_display.short_description = 'Cidade'

#tem que colocar igual abaixo para aparecer no admin
admin.site.register(Brand, BrandAdmin)




@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    form = MecanicoModelForm
    list_display = ['name', 'cidade', 'bairro', 'get_estabelecimento_display', 'carros_Trabalha',]
    search_fields = (
        'name',
        'name_fantasy',
        'cidade__nome' ,
        'bairro'
    )

    autocomplete_fields = ('carros_Trabalha', 'cidade')

    def get_estabelecimento_display(self, obj):
        return obj.name_fantasy

    get_estabelecimento_display.short_description = 'Estabelecimento'

