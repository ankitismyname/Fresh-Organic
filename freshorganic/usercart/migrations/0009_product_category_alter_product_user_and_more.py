# Generated by Django 5.0.1 on 2024-09-06 08:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercart', '0008_product_quantity_product_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('vegetables', 'Vegetables'), ('fruits', 'Fruits'), ('dry_fruits', 'Dry Fruits')], default='vegetables', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='unique_product_per_user'),
        ),
    ]
