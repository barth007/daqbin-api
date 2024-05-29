from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404

from .models import Bin, User, BinData, UserAddress
from .serializers import BinSerializer, UserSerializer, BinDataSerializer, UserAddressSerializer

    
class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """
      A custom viewset providing `create`, `list` `retrieve` and `destroy` actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserAddressViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """
      A custom viewset providing `create`, `list` `retrieve` and `destroy` actions
    """
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    


class BinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """
    A custom viewset providing `create`, `list` `retrieve` and `destroy` actions
    """
    queryset = Bin.objects.all()
    serializer_class = BinSerializer


class BinDataViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """
    A custom viewset providing `create`, `list` `retrieve` and `destroy` actions
    """
    queryset = BinData.objects.all()
    serializer_class = BinDataSerializer

