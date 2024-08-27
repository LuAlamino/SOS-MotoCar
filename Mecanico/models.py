from django.db import models
from carros.models import  Brand

# Create your models here.
class Mecanico(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    name_fantasy = models.CharField(max_length=150, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    carros_Trabalha = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='CarroQue_trabalha', blank=True, null=True)
    Foto_Estabelecimento = models.ImageField(upload_to='Mecanico/Foto_estabelecimento/' ,blank=True, null=True)

#Abaixo agora quando aparecer o nome do mecanico, vai aparecer o nome do mecanico normal, caso tire isso
#vai vir com o nome do mecanico com 'object' junto
    def __str__(self):
        return self.name
