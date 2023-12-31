# Generated by Django 4.2 on 2023-08-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ira', '0008_alter_week_options_week_binance_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='bcc_card',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='week',
            name='bcc_cny',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='week',
            name='bcc_eur',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='week',
            name='bcc_kzt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='week',
            name='bcc_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='week',
            name='binance_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='week',
            name='kaspi_card',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='week',
            name='tabys_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
