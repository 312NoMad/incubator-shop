from rest_framework.serializers import ModelSerializer

from .models import Product, Category


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'image', 'url')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'products', 'url')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['products'] = ProductSerializer(instance.products.all(), many=True, context=self.context).data
        return rep


