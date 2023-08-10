import decimal
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя категории')
    symbol = models.CharField(max_length=10)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Week(models.Model):
    week_number = models.IntegerField(verbose_name='Номер недели', blank=True, editable=False)
    date = models.DateField(verbose_name='Дата')
    

    # kaspi
    kaspi_card = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="Kaspi Card")
    kaspi_deposit_kzt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="Kaspi Deposit KZT")
    kaspi_deposit_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="Kaspi Deposit USD")



    # bcc
    bcc_card = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="BCC Card")
    bcc_kzt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="BCC KZT")
    # bcc_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="Text")
    # bcc_eur = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="Text")
    # bcc_cny = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="Text")

    # binance_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="Text")
    # tabys_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, verbose_name="Text")

    # total_kaspi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, editable=False, verbose_name="Total Kaspi KZT")
    # total_bcc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, editable=False, verbose_name="Text")

    total_kzt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, editable=False, verbose_name="Total ₸")
    total_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, editable=False, verbose_name="Total $")
    total_eur = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, editable=False, verbose_name="Total €")
    total_cny = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True, editable=False, verbose_name="Total ¥")
    
    def save(self, *args, **kwargs):
        if not self.week_number:
            _, week_num, _ = self.date.isocalendar()
            self.week_number = week_num

            if self.kaspi_card is None:
                self.kaspi_card = decimal.Decimal('0.0')
            if self.kaspi_deposit_kzt is None:
                self.kaspi_deposit_kzt = decimal.Decimal('0.0')
            if self.kaspi_deposit_usd is None:
                self.bcc_kzt = decimal.Decimal('0.0')

            self.total_kaspi = self.kaspi_card + self.kaspi_deposit_kzt + (self.kaspi_deposit_usd * 440)



        super().save(*args, **kwargs)

    def clean(self):
        self.week_number = None  # Защита от ручного изменения

    def __str__(self):
        return f"Week {self.week_number}"

    class Meta:
        ordering = ('date',)

        verbose_name = 'Неделю'
        verbose_name_plural = 'Недели'