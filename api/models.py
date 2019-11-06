from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Voucher(models.Model):
    code = models.CharField(max_length=20)
    sale = models.IntegerField()
    active = models.BooleanField(default=True)


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to='avata/', null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def all(self):
        return ProfileUser.objects.all()

    def __str__(self):
        return self.user.username
