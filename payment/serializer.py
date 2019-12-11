from rest_framework import serializers
from .models import PayPalTransaction, CreditCardTransaction


class PayPalTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayPalTransaction
        fields = '__all__'


class CreditCardTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCardTransaction
        fields = '__all__'
