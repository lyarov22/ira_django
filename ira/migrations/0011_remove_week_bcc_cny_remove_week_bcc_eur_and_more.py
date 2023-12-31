# Generated by Django 4.2 on 2023-08-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ira', '0010_alter_week_kaspi_deposit_kzt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week',
            name='bcc_cny',
        ),
        migrations.RemoveField(
            model_name='week',
            name='bcc_eur',
        ),
        migrations.RemoveField(
            model_name='week',
            name='bcc_usd',
        ),
        migrations.RemoveField(
            model_name='week',
            name='binance_total',
        ),
        migrations.RemoveField(
            model_name='week',
            name='tabys_total',
        ),
        migrations.RemoveField(
            model_name='week',
            name='total_bcc',
        ),
        migrations.RemoveField(
            model_name='week',
            name='total_cny',
        ),
        migrations.RemoveField(
            model_name='week',
            name='total_eur',
        ),
        migrations.RemoveField(
            model_name='week',
            name='total_kzt',
        ),
        migrations.RemoveField(
            model_name='week',
            name='total_usd',
        ),
        migrations.AlterField(
            model_name='week',
            name='bcc_card',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='bcc_kzt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='kaspi_card',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='kaspi_deposit_kzt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='kaspi_deposit_usd',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
