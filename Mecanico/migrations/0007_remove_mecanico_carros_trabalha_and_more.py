# Generated by Django 5.1 on 2024-09-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mecanico', '0006_mecanico_informacoes'),
        ('carros', '0005_car_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mecanico',
            name='carros_Trabalha',
        ),
        migrations.AddField(
            model_name='mecanico',
            name='carros_Trabalha',
            field=models.ManyToManyField(blank=True, null=True, related_name='CarroQue_trabalha', to='carros.brand'),
        ),
    ]
