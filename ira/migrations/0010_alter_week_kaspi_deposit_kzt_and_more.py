# Generated by Django 4.2 on 2023-08-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ira', '0009_alter_week_bcc_card_alter_week_bcc_cny_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='kaspi_deposit_kzt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='week',
            name='kaspi_deposit_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
