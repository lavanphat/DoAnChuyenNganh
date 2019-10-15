from rest_framework import serializers

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
        fields = ['id', 'title', 'Price_New', 'image_product']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title','slug', 'url']
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
        fields = '__all__'
