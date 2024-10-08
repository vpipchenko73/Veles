# Generated by Django 4.2.11 on 2024-07-12 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0009_post_category_alter_adress_find_date_find_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress_find',
            name='date_find',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 20, 58, 20, 396341), verbose_name='Дата обнаружения'),
        ),
        migrations.AlterField(
            model_name='adress_owner',
            name='date_location',
            field=models.DateField(default=datetime.datetime(2024, 7, 12, 20, 58, 20, 397356), verbose_name='Дата передачи владельцу'),
        ),
        migrations.AlterField(
            model_name='health',
            name='date_vaccination',
            field=models.DateField(default=datetime.datetime(2023, 7, 7, 20, 58, 20, 397356), verbose_name='Дата прививки'),
        ),
        migrations.AlterField(
            model_name='health',
            name='date_worms',
            field=models.DateField(default=datetime.datetime(2023, 7, 7, 20, 58, 20, 397356), verbose_name='Дата приема глистогонного'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('H', 'Уже дома'), ('R', 'Обычная')], default='R', max_length=20, verbose_name='Категория новости'),
        ),
        migrations.AlterField(
            model_name='post',
            name='datа_creation',
            field=models.DateField(default=datetime.datetime(2024, 7, 12, 20, 58, 20, 398461), verbose_name='Дата создания новости'),
        ),
    ]
