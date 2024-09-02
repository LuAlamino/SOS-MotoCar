from django.shortcuts import render, redirect, redirect, get_object_or_404


from Mecanico.views import new_mecanico_view
from carros.models import Car
from carros.forms import CarModelForm


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


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')

    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})