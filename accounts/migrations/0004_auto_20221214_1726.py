# Generated by Django 3.1.5 on 2022-12-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20221214_1417'),
        ('accounts', '0003_auto_20221214_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='product_favorites',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]