# Generated by Django 5.0.1 on 2024-09-06 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercart', '0006_product_proimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShoppingCartItem',
        ),
    ]
