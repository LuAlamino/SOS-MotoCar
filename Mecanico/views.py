from django.shortcuts import render
from Mecanico.models import Mecanico
from carros.models import Car


def mecanico_view(request):
    mecanico = Mecanico.objects.all()
    search = request.GET.get('search')
    if search:
        mecanico = mecanico.filter(model__icontains=search)

    print(mecanico)


    return render(request,
    'mecanico.html',
        {'mecanico': mecanico})

