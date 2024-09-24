

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from Mecanico.forms import MecanicoForm, MecanicoModelForm
from Mecanico.models import Mecanico
from carros.models import Car
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


#Substitui o mecanico_view pelo MecanicoListView
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


class MecanicoListView(ListView):
    model = Mecanico
    template_name = 'mecanico.html'
    context_object_name = 'mecanico'

    def get_queryset(self):
        mecanico = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
            mecanico = mecanico.filter(bairro__icontains=search)

        return mecanico

@method_decorator(login_required(login_url='login'), name='dispatch')
class MecanicoCreateView(CreateView):
    model = Mecanico
    form_class = MecanicoModelForm
    template_name = 'new_mecanico.html'
    success_url = '/mecanico/'


class MecanicoDetailView(DetailView):
    model = Mecanico
    template_name = 'mecanico_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class MecanicoUpdateView(UpdateView):
    model = Mecanico
    form_class = MecanicoModelForm
    template_name = 'mecanico_update.html'
    success_url = '/mecanico/'

    def get_success_url(self):
        return reverse_lazy('mecanico_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class MecanicoDeleteView(DeleteView):
    model = Mecanico

    template_name = 'mecanico_delete.html'
    success_url = reverse_lazy('mecanico_list')

