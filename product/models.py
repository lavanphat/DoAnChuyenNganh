from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator


# Create your models here.


class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tên Thương Hiệu')
    slug = models.SlugField(verbose_name='Từ khóa thương hiệu', unique=True, blank=True)
    Image = models.ImageField(verbose_name='Hình Sản Phẩm', blank=True, null=True, upload_to='images/')
    Image_URL = models.CharField(max_length=255, verbose_name='Link Hình', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Thương Hiệu'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tên Loại')
    slug = models.SlugField(verbose_name='Từ khóa loại', unique=True, blank=True)
    Image = models.ImageField(verbose_name='Hình loại', blank=True, null=True, upload_to='images/')
    Image_URL = models.CharField(max_length=255, verbose_name='Link Hình', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Loại Sản Phẩm'


class Product(models.Model):
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Thương Hiệu',related_name='product')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Loại', blank=True, null=True,related_name='product')
    title = models.CharField(max_length=255, verbose_name='Tên Sản Phẩm')
    slug = models.SlugField(verbose_name='Từ Khóa Sản Phẩm', unique=True, blank=True)
    Price_Import = models.DecimalField(verbose_name='Giá Nhập Hàng', decimal_places=0, max_digits=10)
    Price_Old = models.DecimalField(verbose_name='Giá Bán ', decimal_places=0, max_digits=10)
    Price_New = models.DecimalField(verbose_name='Giá Khuyến Mãi', decimal_places=0, max_digits=10)
    Wage = models.DecimalField(verbose_name='Tiền Công', decimal_places=0, max_digits=10)
    Quality = models.IntegerField(verbose_name='Số Lượng Còn')
    Decription = models.TextField(verbose_name='Mô Tả')
    Date_Create = models.DateTimeField(auto_now_add=True, verbose_name='Ngày Tạo')
    Date_Update = models.DateTimeField(auto_now=True, verbose_name='Ngày Sửa')
    Active = models.BooleanField(default=True, verbose_name='Kích Hoạt')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sản Phẩm'


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tên Dịch Vụ')
    Price = models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Giá')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Từ Khóa Dịch Vụ')
    Active = models.BooleanField(verbose_name='Kích Hoạt', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Dịch Vụ'


class Banner(models.Model):
    Image = models.CharField(verbose_name='Banner', max_length=1000)
    Number = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(3)],
                                 unique=True)


class Image_Product(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_product')
    Image = models.ImageField(verbose_name='Hình Sản Phẩm', upload_to='images/', null=True, blank=True)
    Image_URL = models.CharField(max_length=255, verbose_name='Link Hình', blank=True, null=True)

    # def __str__(self):
    #     return self.Image_URL


def slug_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_pre_save, sender=Brand)
pre_save.connect(slug_pre_save, sender=Product)
pre_save.connect(slug_pre_save, sender=Service)
pre_save.connect(slug_pre_save, sender=Category)
