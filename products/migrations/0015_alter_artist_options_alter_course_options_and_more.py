# Generated by Django 4.2.2 on 2023-07-07 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_artist_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Мастера', 'verbose_name_plural': 'Мастера'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курсы', 'verbose_name_plural': 'Курс'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказ'},
        ),
    ]
