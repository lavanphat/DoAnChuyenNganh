# Create your views here.
from rest_framework.viewsets import ModelViewSet

from api.serializers import *


class BannerViewSet(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    http_method_names = ['get',]

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ['get',]
