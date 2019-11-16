# Create your views here.
from django_filters import rest_framework as filters
from pusher_push_notifications import PushNotifications
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
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
    # queryset = Bill.objects.all().order_by('-Date_Create')
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'id'

    # serializer_class = BillWithProductSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return BillSerializer
        if self.action == 'retrieve':
            return BillWithProductSerializer
        return BillWithProductSerializer

    def create(self, request, *args, **kwargs):
        bill = BillSerializer(data=request.data, context={'request': request})
        # user = User.objects.get(username__iexact=request.data["user"]).pk
        if bill.is_valid():
            bill.User = request.POST.get('User')
            bill.save()
            return Response(bill.data, status=status.HTTP_201_CREATED)
        return Response(bill.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Bill.objects.all().order_by('-Date_Create')
        user = self.request.query_params.get('User')
        status_bill = self.request.query_params.get('Status_Bill')

        if user:
            queryset = Bill.objects.filter(User=user, Status_Bill__iexact=status_bill).order_by('-Date_Create')
        return queryset
    # def perform_create(self, serializer):
    #     serializer.validated_data['User'] = self.request.user
    #     return super(BillViewSet, self).perform_create(serializer)


class BillProductViewSet(ModelViewSet):
    # queryset = Bill_Product.objects.all().order_by('-Bill')
    http_method_names = ['get', 'post', 'delete']
    # lookup_field = 'id'
    serializer_class = BillProductSerializer

    def get_queryset(self):
        queryset = Bill_Product.objects.all().order_by('-Bill')
        bill = self.request.query_params.get('Bill')

        if bill:
            queryset = Bill_Product.objects.filter(Bill__exact=bill).order_by('-Bill')
        return queryset


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
        elif self.action == 'retrieve':
            return UserPutSerializer
        return UserPostSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.query_params.get('username')

        if user:
            queryset = User.objects.filter(username__exact=user)
        return queryset


class ProfileUserViewSet(ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileUserSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username and password:
            user_obj = User.objects.filter(username__iexact=username)
            if user_obj.exists() and user_obj.first().check_password(password):
                user = LoginSerializer(user_obj, many=True)

                try:
                    profile = [
                        {
                            "id": user.data[0]['profile'][0]['id'],
                            "image": user.data[0]['profile'][0]['image'],
                            "phone": user.data[0]['profile'][0]['phone'],
                            "address": user.data[0]['profile'][0]['address'],
                        }
                    ]
                except TypeError:
                    profile = []

                data_list = {
                    'id': user.data[0]['id'],
                    'username': user.data[0]['username'],
                    "password": user.data[0]['password'],
                    "first_name": user.data[0]['first_name'],
                    "last_name": user.data[0]['last_name'],
                    "email": user.data[0]['email'],
                    "profile": profile
                }
                return Response(data_list)
            else:
                return Response({'message': 'login failed'})
        else:
            return Response({'message': 'form invalid'})


class SearchFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'title': ['icontains'],
            'Price_New': ['gte', 'lte']
        }


class SearchViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', ]
    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_class = SearchFilter
    ordering_fields = ['Price_New', ]


class NotificationsViewSet(ModelViewSet):
    http_method_names = ['post', ]
    serializer_class = NotificationsSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        notifications = NotificationsSerializer(data=request.data, context={'request': request})
        if notifications.is_valid():
            beams_client = PushNotifications(
                instance_id='746eae18-a178-4f92-9bf7-61fd8cbaff9e',
                secret_key='84FCCBE1590FC5652373F9860C04F7BCD809DE04CCBE63D451E4F81043B13FDE',
            )
            response = beams_client.publish_to_interests(
                interests=['hello'],
                publish_body={
                    'apns': {
                        'aps': {
                            'alert': 'Notifications created!'
                        }
                    },
                    'fcm': {
                        'notification': {
                            'title': request.POST.get('title'),
                            'body': request.POST.get('content')
                        }
                    }
                }
            )
            print(response['publishId'])
        return Response(notifications.errors, status=status.HTTP_400_BAD_REQUEST)
