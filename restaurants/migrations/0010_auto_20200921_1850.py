# Generated by Django 3.1.1 on 2020-09-22 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_auto_20200921_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]