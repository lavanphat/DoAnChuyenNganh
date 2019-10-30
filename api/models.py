from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Voucher(models.Model):
    code = models.CharField(max_length=20)
    sale = models.IntegerField()
    active = models.BooleanField(default=True)


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avata/')
