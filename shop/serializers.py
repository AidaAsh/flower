from rest_framework import serializers
from shop.models import *


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'


class CompositionSerializer(serializers.ModelSerializer):
    flower = serializers.CharField(source='id_flower.title', read_only=True)
    product = serializers.CharField(source='id_product.title', read_only=True)

    class Meta:
        model = Composition
        fields = ('id', 'id_flower', 'flower', 'id_product', 'product')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(source='id_order', read_only=True)
    product_title = serializers.CharField(source='id_product', read_only=True)
    product_price = serializers.CharField(source='id_product.price', read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'id_order', 'order_number', 'id_product', 'product_title', 'product_price', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_number',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    label = LabelSerializer(many=True, read_only=True)
    composition = CompositionSerializer(many=True, source='composition_product', read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('pk', 'title', 'price', 'image', 'description', 'category', 'label', 'composition', 'reviews')


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = '__all__'
