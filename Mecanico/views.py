from django.shortcuts import render, redirect

from Mecanico.forms import MecanicoForm
from Mecanico.models import Mecanico
from carros.models import Car


def mecanico_view(request):
    mecanico = Mecanico.objects.all()
    search = request.GET.get('search')
    if search:
        mecanico = mecanico.filter(name__icontains=search)

    print(mecanico)


    return render(request,
    'mecanico.html',
        {'mecanico': mecanico})

def new_mecanico_view(request):
    if request.method == 'POST':
        new_mecanico_form = MecanicoForm(request.POST, request.FILES)
        if new_mecanico_form.is_valid():
            new_mecanico_form.save()
            return redirect('mecanico_list')
    else:
        new_mecanico_form = MecanicoForm()
    return render(request, 'new_mecanico.html',{'new_mecanico_form': new_mecanico_form})
