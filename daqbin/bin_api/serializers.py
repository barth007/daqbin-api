from rest_framework import serializers
from .models import Bin, User, BinData, UserAddress

class BinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bin
        exclude = ['is_bin_asigned']

      
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
        
class BinDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BinData
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['user_id', 'house_no', 'street', 'city', 'country']