# Generated by Django 4.0.4 on 2022-05-22 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_alter_product_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='item',
            new_name='Product',
        ),
    ]