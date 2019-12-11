from django.db import models
from django.utils import timezone

from registration.models import Consumer, Caterer


# Create your models here.
class PayPalTransaction(models.Model):
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE)
    holder = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    paypal_username = models.CharField(max_length=100)
    date_transacted = models.DateTimeField()

    def __str__(self):
        return 'Holder: {} {}'.format(
            self.holder.first_name,
            self.holder.last_name
        )

    def save(self, *args, **kwargs):
        if self.date_transacted is None:
            self.date_transacted = timezone.now()
        return super(PayPalTransaction, self).save(*args, **kwargs)


class CreditCardTransaction(models.Model):
    card_number = models.CharField(max_length=100)
    card_holder = models.CharField(max_length=100)
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    date_transacted = models.DateTimeField()
    expiration_date = models.DateTimeField()
    cvv = models.CharField(max_length=100)

    def __str__(self):
        return 'Holder: {} {}'.format(
            self.consumer.first_name,
            self.consumer.last_name
        )

    def save(self, *args, **kwargs):
        if self.date_transacted is None:
            self.date_transacted = timezone.now()
        return super(CreditCardTransaction, self).save(*args, **kwargs)
