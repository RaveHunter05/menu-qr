# Generated by Django 3.1.1 on 2020-09-22 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_auto_20200921_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(default=''),
        ),
    ]