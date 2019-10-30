from rest_framework import serializers

from api.models import Voucher
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
    # Product = serializers.SerializerMethodField()

    class Meta:
        model = Bill_Product
        fields = ['id', 'Bill', 'Product', 'Quality', ]

    # def get_Product(self, obj):
    #     return obj.Product.title


class BillSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Bill
        fields = ['url', 'Date_Create', 'Total_Money', 'Sale', 'Address', 'Phone', 'Active', 'user', ]
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    def get_user(self, obj):
        return obj.User.username


class BillWithProductSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    product = BillProductSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ['url', 'Date_Create', 'Total_Money', 'Sale', 'Address', 'Phone', 'product', 'Active', 'user', ]
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    def get_user(self, obj):
        return obj.User.username

    def get_product(self, obj):
        return obj.Product.title


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ['url', 'code', 'sale']
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }
