from django.urls import path
from .views import BinAPI, UserAPI, UserDetailAPI, BinDataAPI, BinParametersAPI

urlpatterns = [
    path('api/', UserAPI.as_view()),
    path('api/create-user/', UserAPI.as_view()),
    path('api/user/<str:pk>/', UserDetailAPI.as_view()),
    path('api/bins/', BinAPI.as_view()),
    path('api/create-bin/', BinAPI.as_view()),
    #
    path('api/update-bin/', BinDataAPI.as_view()),
    path('api/bin-para/', BinDataAPI.as_view()),
    path('api/bin-parameter/<str:pk>/', BinParametersAPI.as_view()),
]