# Generated by Django 4.2.2 on 2023-07-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_order_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
    ]
