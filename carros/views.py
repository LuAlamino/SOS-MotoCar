from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from Mecanico.views import new_mecanico_view
from carros.models import Car
from carros.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, UpdateView, DeleteView


#A carros_view a baixo foi substituida pela CarsView
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

# a def new_car_view vou substituida pela class NewCarView
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')

    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})

#Metodo utilizando View porem vou utilizar o ListView
class CarsView(View):
    def get(self, request):
        carros = Car.objects.all().order_by('model')
        search = request.GET.get('search')
        if search:
            carros = carros.filter(model__icontains=search)
        return render(
            request,
            'carros.html',
            {'carros': carros}
        )




class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )



#Substitui a CarView pela CarListView
class CarListView(ListView):
    model = Car
    context_object_name = 'carros'
    template_name = 'carros.html'

# utilizo o super() para acessar o Car, se fosse self
#So buscaria do get_queryset
    def get_queryset(self):
        carros = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            carros = carros.filter(model__icontains=search)
        return carros
#Essa função method_decorator, somente quem estiver logado pode acesar esse metodo
@method_decorator(login_required(login_url='login'), name='dispatch')
# vou substituir a NewCarView pela NewCarCreatView
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/carros/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/carros/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_delete.html'
    success_url = '/carros/'