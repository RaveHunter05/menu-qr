# Generated by Django 3.1.1 on 2020-09-26 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0017_auto_20200925_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='path/to/my/default/image.jpg', upload_to='media/'),
        ),
    ]
