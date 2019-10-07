from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter()
router.register('banner', BannerViewSet, base_name='banner')
router.register('category', CategoryViewSet, base_name='category')

urlpatterns = [
    path('', include(router.urls)),

]
