# Generated by Django 2.2.6 on 2020-09-15 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Nombre de Categoría')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Última actualización')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Última actualización')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Última actualización')),
            ],
            options={
                'verbose_name': 'Restaurante',
                'verbose_name_plural': 'Restaurantes',
            },
        ),
        migrations.CreateModel(
            name='MenuDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Producto')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Última actualización')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Category', verbose_name='Categoría')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Menu', verbose_name='Menú')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant', unique=True),
        ),
    ]
