from django.contrib import admin

# Register your models here.
from api.models import Voucher


class VoucherAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'sale')


admin.site.register(Voucher, VoucherAdmin)
