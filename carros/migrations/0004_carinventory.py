# Generated by Django 5.1 on 2024-09-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0003_cidade_car_cidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cars_value', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]