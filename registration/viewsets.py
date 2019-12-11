from rest_framework import viewsets
from .models import Caterer, Consumer, CatrUser, Menu, Item, Transaction, Package, Image
from .serializer import CatererSerializer,\
    ConsumerSerializer,\
    CatrUserSerializer,\
    MenuSerializer,\
    ItemSerializer,\
    TransactionSerializer,\
    PackageSerializer,\
    ImageSerializer


class CatererViewSet(viewsets.ModelViewSet):
    queryset = Caterer.objects.all()
    serializer_class = CatererSerializer


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class CatrUserViewSet(viewsets.ModelViewSet):
    queryset = CatrUser.objects.all()
    serializer_class = CatrUserSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
