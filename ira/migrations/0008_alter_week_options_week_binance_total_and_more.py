# Generated by Django 4.2 on 2023-08-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ira', '0007_alter_week_options_alter_week_week_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ('date',), 'verbose_name': 'Неделю', 'verbose_name_plural': 'Недели'},
        ),
        migrations.AddField(
            model_name='week',
            name='binance_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='tabys_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_bcc',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_cny',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_eur',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_kaspi',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_kzt',
            field=models.DecimalField(blank=True, decimal_places=2, default=111, editable=False, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='total_usd',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, editable=False, max_digits=10),
            preserve_default=False,
        ),
    ]