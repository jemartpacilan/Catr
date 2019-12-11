from rest_framework import serializers
from .models import Caterer, Consumer, CatrUser, Menu, Item, Transaction, Package, Image


class CatererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caterer
        fields = '__all__'


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'


class CatrUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatrUser
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'