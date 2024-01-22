from django.urls import path
from .views import BinAPI, UserAPI, UserDetailAPI, BinDataAPI, BinParametersAPI

urlpatterns = [
    path('api/', UserAPI.as_view()),
    path('api/user/create/', UserAPI.as_view()),
    path('api/del-user/<str:pk>/', UserAPI.as_view()),
    path('api/user/<str:pk>/', UserDetailAPI.as_view()),
    path('api/bins/', BinAPI.as_view()),
    path('api/bin/create/', BinAPI.as_view()),
    path('api/bin/<str:pk>/', BinAPI.as_view()),
    path('api/sensordata/update/', BinDataAPI.as_view()),
    path('api/sensordata/', BinDataAPI.as_view()),
    path('api/sensordata<str:pk>/', BinParametersAPI.as_view()),
]