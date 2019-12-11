from django.db import models
from django.utils import timezone

from registration.models import Caterer, Consumer


# Create your models here.
class Message(models.Model):
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    message_body = models.CharField(max_length=1000)
    message_date_submitted = models.DateTimeField()
    message_owned_by_consumer = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.message_date_submitted is None:
            self.message_date_submitted = timezone.now()
        return super(Message, self).save(*args, **kwargs)
