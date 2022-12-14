# Generated by Django 4.1 on 2022-11-08 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiendita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(help_text='Ingrese el nombre del producto', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(help_text='Ingrese cantidad en stock', null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiendita.categoria'),
        ),
    ]
