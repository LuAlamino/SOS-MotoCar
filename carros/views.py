from django.shortcuts import render
from carros.models import Car



def carros_view(request):
    carros = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        carros = carros.filter(model__icontains=search)
    print(carros)

# Posso tirar o '.all' e colocar 'filter()' e colocar filtros, como ".filter(brand=1) e assim ira mostrar apenas as marcas salvas com o codigo 1
# Posso utilizar 'filter(brand__name='Fiat') assim vai trazer pelo nome por conta de ser ForeignKey.
# utilizar o "model='nome do modelo'" ele deve ser exatamente igual ao que esta no campo
# Porem se usar 'model__icontains' ele nao diferencia de letras minuscula ou maiuscula
# na URL para usar de filtro utilizar "?search=Nome que queira"


    return render(request, 'carros.html', {'carros': carros})
