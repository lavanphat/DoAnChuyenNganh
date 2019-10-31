from django.contrib.auth.models import User
from django.db import models

from product.models import Product, Service


# Create your models here.
class Bill(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Người Tạo', blank=True, null=True)
    Date_Create = models.DateTimeField(auto_now_add=True, verbose_name='Ngày Tạo')
    Total_Money = models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Tổng Tiền', default=0)
    Sale = models.IntegerField(default=0, verbose_name='Giảm Giá')
    Address = models.CharField(max_length=255, verbose_name='Địa Chỉ Nhận', blank=True, null=True)
    Phone = models.CharField(max_length=10, verbose_name='Số Điện Thoại', blank=True, null=True)
    Status_Bill = models.CharField(max_length=50, choices=(
        ('processing', 'Đang xử lí'),
        ('confirmed', 'Đã xác nhận'),
        ('delivery', 'Đang giao hàng'),
        ('has_delivered', 'Đã giao'),
        ('cancelled', 'Đã hủy'),
        ('returns', 'Trả hàng')
    ), default='processing')
    Active = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.User

    class Meta:
        verbose_name_plural = 'Hóa Đơn'


class Bill_Product(models.Model):
    Bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='product')
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Sản Phẩm')
    Quality = models.IntegerField(default=1, verbose_name='Số Lượng')

    class Meta:
        verbose_name_plural = 'Hóa Đơn Sản Phầm'


class Bill_Service(models.Model):
    Bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    Service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Quality = models.IntegerField(default=1, verbose_name='Số Lượng')

    class Meta:
        verbose_name_plural = 'Hóa Đơn Dịch Vụ'
