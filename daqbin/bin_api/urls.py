from django.urls import path
from .views import BinViewSet, BinDataViewSet, UserAddressViewSet, UserViewSet
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
router.register(r'api/v1/users', UserViewSet, basename='users')
router.register(r'api/v1/user_address', UserAddressViewSet, basename='user_address')
router.register(r'api/v1/bins', BinViewSet, basename='bins')
router.register(r'api/v1/bin_data', BinDataViewSet, basename='bin_data')

urlpatterns = router.urls

# urlpatterns = [
#     path('api/', UserAPI.as_view()),
#     path('api/user/create/', UserAPI.as_view()),
#     path('api/del-user/<str:pk>/', UserAPI.as_view()),
#     path('api/user/<str:pk>/', UserDetailAPI.as_view()),
#     path('api/bins/', BinAPI.as_view()),
#     path('api/bin/create/', BinAPI.as_view()),
#     path('api/bin/<str:pk>/', BinAPI.as_view()),
#     path('api/sensordata/update/', BinDataAPI.as_view()),
#     path('api/sensordata/', BinDataAPI.as_view()),
#     path('api/sensordata<str:pk>/', BinParametersAPI.as_view()),
# ]