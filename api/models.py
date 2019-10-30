from django.db import models


# Create your models here.
class Voucher(models.Model):
    code = models.CharField(max_length=20)
    sale = models.IntegerField()
    active = models.BooleanField(default=True)
