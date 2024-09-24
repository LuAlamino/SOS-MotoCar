# Aqui vou colocar informações que vao ser salvas
# antes de salvar algo ou depois de salvar no banco de dados

from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

from Mecanico.models import Mecanico, MecanicoRegistro
from django.core.exceptions import ValidationError
from carros.models import Car



def mecanico_inventory_update():
    mecanico_counts = Mecanico.objects.all().count()

    MecanicoRegistro.objects.create(
        mecanico_count = mecanico_counts,
    )


@receiver(pre_save, sender=Mecanico)
def mecanico_pre_save(sender, instance, **kwargs):
    if not instance.informacoes:
        instance.informacoes = 'A bio não foi informada.'



        '''ai_informacoes = get_mecanico_ai_bio(
            instance.name_fantasy, instance.cidade
        )
        instance.informacoes = ai_informacoes
        '''

@receiver(post_save, sender=Mecanico)
def mecanico_post_save(sender, instance, **kwargs):
    mecanico_inventory_update()

@receiver(post_delete, sender=Mecanico)
def mecanico_post_delete(sender, instance, **kwargs):
    mecanico_inventory_update()





