from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter()
router.register('banner', BannerViewSet, base_name='banner')
router.register('category', CategoryViewSet, base_name='category')
router.register('product featured', ProductFeaturedViewSet, base_name='product featured')

urlpatterns = [
    path('', include(router.urls)),

]
