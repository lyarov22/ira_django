# Generated by Django 4.2 on 2023-08-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ira', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
    ]
