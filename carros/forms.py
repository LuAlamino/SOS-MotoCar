from django import forms
from carros.models import Brand, Car

# eu estou usando o forms abaixo o CarModelForm , poiss esse CarForm é um jeito manual de trazer os campos
#ja o CarModelForm é a maneira mais clean do django
class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    Plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            Plate = self.cleaned_data['Plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car

#Uma forma bem mais simples de pega o formulario
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
# 'clean_' é uma função de validação ,
# entao posso colocar "clean_" e mais o campo que eu deseja do meu banco de dados
# no exemplo eu vou utilizar o campo valor 'value'
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$5.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1500:
            self.add_error('factory_year', 'Não é possivel cadastrar carros fabricados antes de 1500')
        return factory_year

#por isso coloco o campo if new_car_form.is_valid(): pois se nao for valido conforme os campos acima
#ele ira informar os erros