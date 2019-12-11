from rest_framework import viewsets
from .models import PayPalTransaction, CreditCardTransaction
from .serializer import PayPalTransactionSerializer, CreditCardTransactionSerializer


class PayPalTransactionViewSet(viewsets.ModelViewSet):
	queryset = PayPalTransaction.objects.all()
	serializer_class = PayPalTransactionSerializer


class CreditCardTransactionSerializer(viewsets.ModelViewSet):
	queryset = CreditCardTransaction.objects.all()
	serializer_class = CreditCardTransactionSerializer
