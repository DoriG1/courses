# Generated by Django 4.2.2 on 2023-07-07 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_order_course_alter_order_date_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Мастера', 'verbose_name_plural': 'Мастер'},
        ),
    ]