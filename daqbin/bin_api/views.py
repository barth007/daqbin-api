from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

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


    @action(detail=False, methods=['get'], url_path='unique-id/(?P<bin_unique_id>[^/.]+)')
    def get_bindata_by_id(self, request, bin_unique_id=None):
      bin=get_object_or_404(Bin, bin_unique_id=bin_unique_id)
      bindata = BinData.objects.filter(the_bin=bin)
      serializer = self.get_serializer(bindata, many=True)
      return Response(serializer.data)

