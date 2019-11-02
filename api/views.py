# Create your views here.
from rest_framework.viewsets import ModelViewSet

from api.serializers import *


class BannerViewSet(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    http_method_names = ['get', ]


class ProductFeaturedViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(Active=True).order_by('-Date_Create')[:10]
    http_method_names = ['get', ]


class CategoryViewSet(ModelViewSet):
    # serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ['get', ]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        if self.action == 'retrieve':
            return ProductInCategorySerializer


class BrandViewSet(ModelViewSet):
    # serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    http_method_names = ['get', ]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return BrandSerializer
        if self.action == 'retrieve':
            return ProductInBranSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(Active=True)
    http_method_names = ['get', ]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductAllSerializer
        if self.action == 'retrieve':
            return ProductSerializer


class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all().order_by('-Date_Create')
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'id'

    # serializer_class = BillWithProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BillSerializer
        if self.action == 'retrieve':
            return BillWithProductSerializer
        return BillWithProductSerializer


class BillProductViewSet(ModelViewSet):
    queryset = Bill_Product.objects.all().order_by('-Bill')
    http_method_names = ['get', 'post', 'delete']
    # lookup_field = 'id'
    serializer_class = BillProductSerializer


class VoucherViewSet(ModelViewSet):
    queryset = Voucher.objects.filter(active=True)
    http_method_names = ['get', 'post']
    serializer_class = VoucherSerializer
    lookup_field = 'id'


class UserViewSet(ModelViewSet):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put']
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'create':
            return UserPostSerializer
        elif self.action == 'update':
            return UserPutSerializer
        return UserPostSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.query_params.get('username')
        password = self.request.query_params.get('password')

        if user and password:
            queryset = User.objects.filter(username__exact=user, password__exact=password)
        return queryset


class ProfileUserViewSet(ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileUserSerializer
