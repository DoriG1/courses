# Generated by Django 4.2.2 on 2023-07-07 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_artist_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Мастера', 'verbose_name_plural': 'Мастер'},
        ),
    ]
