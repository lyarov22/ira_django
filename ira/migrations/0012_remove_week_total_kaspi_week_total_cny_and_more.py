# Generated by Django 4.2 on 2023-08-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ira', '0011_remove_week_bcc_cny_remove_week_bcc_eur_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week',
            name='total_kaspi',
        ),
        migrations.AddField(
            model_name='week',
            name='total_cny',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10, verbose_name='Total ¥'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_eur',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10, verbose_name='Total €'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_kzt',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10, verbose_name='Total ₸'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_usd',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10, verbose_name='Total $'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='week',
            name='bcc_card',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='BCC Card'),
        ),
        migrations.AlterField(
            model_name='week',
            name='bcc_kzt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='BCC KZT'),
        ),
        migrations.AlterField(
            model_name='week',
            name='kaspi_card',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Kaspi Card'),
        ),
        migrations.AlterField(
            model_name='week',
            name='kaspi_deposit_kzt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Kaspi Deposit KZT'),
        ),
        migrations.AlterField(
            model_name='week',
            name='kaspi_deposit_usd',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Kaspi Deposit USD'),
        ),
    ]