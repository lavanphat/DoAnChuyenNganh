# Create your views here.
from rest_framework.viewsets import ModelViewSet

from api.serializers import *


class BannerViewSet(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    http_method_names = ['get', ]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ['get', ]


class ProductFeaturedViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(Active=True).order_by('-Date_Create')[:10]
    http_method_names = ['get', ]


class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    http_method_names = ['get', ]
