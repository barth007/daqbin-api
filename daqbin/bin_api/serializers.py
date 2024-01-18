from rest_framework import serializers
from .models import Bin, User, BinData

class BinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bin
        fields = '__all__'
      
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
        
class BinDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BinData
        fields = '__all__'