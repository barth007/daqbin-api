from django.urls import path
from .views import BinViewSet, BinDataViewSet, UserAddressViewSet, UserViewSet
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
router.register(r'api/v1/users', UserViewSet, basename='users')
router.register(r'api/v1/user_address', UserAddressViewSet, basename='user_address')
router.register(r'api/v1/bins', BinViewSet, basename='bins')
router.register(r'bin_data', BinDataViewSet, basename='bin_data')

urlpatterns = router.urls