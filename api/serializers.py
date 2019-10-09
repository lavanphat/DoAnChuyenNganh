from rest_framework import serializers

from product.models import Banner, Category, Product, Image_Product, Brand


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Product
        fields = ['Image', 'Image_URL']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image_product = ImageProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'Price_New', 'image_product']
