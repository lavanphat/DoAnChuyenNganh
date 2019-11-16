from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from api.models import Voucher, ProfileUser
from bill.models import Bill, Bill_Product
from product.models import Banner, Category, Product, Image_Product, Brand


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Product
        fields = ['Image', 'Image_URL']


class ProductSerializer(serializers.ModelSerializer):
    image_product = ImageProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'Decription', 'Price_New', 'image_product']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'url']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ProductInCategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'product']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'slug', 'title', 'Image', 'Image_URL', 'url']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ProductInBranSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'product']


class ProductAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'url']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class BillProductSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True,read_only=True)
    slug = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Bill_Product
        fields = ['id', 'Bill', 'Product', 'Quality', 'slug']

    # def get_Product(self, obj):
    #     return obj.Product.title

    def get_slug(self, obj):
        return obj.Product.slug


class BillSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(read_only=True)

    Status_Bill = serializers.CharField(source='get_Status_Bill_display', read_only=True)

    class Meta:
        model = Bill
        fields = ['url', 'Date_Create', 'Total_Money', 'Sale', 'Address', 'Phone', 'Status_Bill', 'Active',
                  'User']
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    # def get_user(self, obj):
    #     if obj.User:
    #         return obj.User.username
    #     else:
    #         return 'null'


class BillWithProductSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    product = BillProductSerializer(many=True, read_only=True)
    Status_Bill = serializers.CharField(source='get_Status_Bill_display', read_only=True)

    class Meta:
        model = Bill
        fields = ['url', 'Date_Create', 'Total_Money', 'Sale', 'Address', 'Phone', 'product', 'Status_Bill', 'Active',
                  'user', ]
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    def get_user(self, obj):
        if obj.User:
            return obj.User.username
        else:
            return 'null'

    # def get_product(self, obj):
    #     return obj.Product.title


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ['url', 'code', 'sale']
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }


class ProfileUserSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = ProfileUser
        # fields = ['id', 'image', 'phone', 'address']
        fields = '__all__'
    # def get_user(self, obj):
    #     if obj.User:
    #         return obj.User.username
    #     else:
    #         return 'null'


class UserPutSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'password', 'first_name', 'last_name', 'email', 'profile']
        # fields = ""
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'},
            'username': {'read_only': 'true'}
        }

    def get_profile(self, obj):
        try:
            serializer = ProfileUserSerializer(obj.profile.all(), many=True)
            print(serializer.data[0]['image'])
            return serializer.data
        except ObjectDoesNotExist:
            return 'null'


class UserPostSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'first_name', 'last_name', 'email', 'profile']
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'},
        }

    def get_profile(self, obj):
        try:
            serializer = ProfileUserSerializer(obj.profile.all(), many=True)
            print(serializer.data[0]['image'])
            return serializer.data
        except ObjectDoesNotExist:
            return 'null'

    def create(self, validated_data):
        user = super(UserPostSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'profile']

    def get_profile(self, obj):
        try:
            serializer = ProfileUserSerializer(obj.profile.all(), many=True)
            print(serializer.data[0]['image'])
            return serializer.data
        except ObjectDoesNotExist:
            return 'null'


class NotificationsSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
    content = serializers.CharField(required=True, max_length=500)
