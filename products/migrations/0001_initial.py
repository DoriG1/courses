# Generated by Django 4.2.2 on 2023-06-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Описание товара')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('price', models.FloatField()),
                ('location', models.CharField(max_length=255, verbose_name='Адрес')),
                ('time', models.CharField(max_length=255, verbose_name='Время')),
                ('date_start', models.CharField(max_length=255, verbose_name='Старт курса')),
            ],
        ),
    ]