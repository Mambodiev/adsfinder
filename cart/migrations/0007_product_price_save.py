# Generated by Django 3.2 on 2021-09-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_rename_comment_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_save',
            field=models.IntegerField(default=0),
        ),
    ]
