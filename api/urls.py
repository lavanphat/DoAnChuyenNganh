from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter()
router.register('banner', BannerViewSet, base_name='banner')
router.register('category', CategoryViewSet, base_name='category')
router.register('product-featured', ProductFeaturedViewSet, base_name='product featured')
router.register('brand', BrandViewSet, base_name='brand')
router.register('product-all', ProductViewSet, base_name='product')
router.register('bill', BillViewSet, base_name='bill')
router.register('bill-product', BillProductViewSet, base_name='bill product')
router.register('voucher', VoucherViewSet, base_name='voucher')

urlpatterns = [
    path('', include(router.urls)),
    # path('voucher/',VoucherAPIView.as_view())
]
