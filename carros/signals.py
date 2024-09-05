# Aqui vou colocar informações que vao ser salvas
# antes de salvar algo ou depois de salvar no banco de dados

from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

from carros.models import Car


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):

    print('### Pré SAVE ###')

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    return ()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    return ()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    return ()