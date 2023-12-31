from rest_framework import serializers
from main import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ('id', 'user', 'address')

    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ('id', 'user', 'address')

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'category', 'vendor', 'title', 'detail', 'price')

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'category', 'vendor', 'title', 'detail', 'price')

    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id', 'user', 'mobile')

    def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id', 'user', 'mobile')

    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
