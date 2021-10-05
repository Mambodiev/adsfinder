# Generated by Django 3.2 on 2021-09-23 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_rename_product_price_product_product_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='specification',
            new_name='short_product_detail',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='specification_en',
            new_name='short_product_detail_en',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='specification_fr',
            new_name='short_product_detail_fr',
        ),
    ]