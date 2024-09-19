from django import forms
from Mecanico.models import Mecanico
from carros.models import Cidade, Brand

class MecanicoForm(forms.Form):
    name = forms.CharField(max_length=100)
    name_fantasy = forms.CharField(max_length=150)

    cidade = forms.ModelChoiceField(Cidade.objects.all())
    bairro = forms.CharField(max_length=100)
    carros_Trabalha = forms.ModelChoiceField(Brand.objects.all())
    Foto_Estabelecimento = forms.ImageField()

    def save(self):
        mecanico = Mecanico(
            name=self.cleaned_data['name'],
            name_fantasy=self.cleaned_data['name_fantasy'],

            cidade=self.cleaned_data['cidade'],
            bairro=self.cleaned_data['bairro'],
            carros_Trabalha=self.cleaned_data['carros_Trabalha'],
            Foto_Estabelecimento=self.cleaned_data['Foto_Estabelecimento'],
        )
        mecanico.save()
        return mecanico
class MecanicoModelForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = '__all__'
        labels = {
            "name" : "Nome",
            "name_fantasy" : "Nome Estabelecimento",
            "bairro" : "Bairro",
            "carros_Trabalha" : "Carros Trabalha",
            "cidade" : "Cidade",

        }