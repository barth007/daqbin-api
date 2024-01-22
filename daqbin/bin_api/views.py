from rest_framework import status
from rest_framework.views import APIView, Response
from .models import Bin, User, BinData
from .serializers import BinSerializer, UserSerializer, BinDataSerializer

# Create your views here.
class UserAPI(APIView):
    
    #Function to get all registered users
    def get(self,request):
        users = User.objects.all() 
        serializedUserData = UserSerializer(users, many=True)
        return Response(serializedUserData.data)
    
     #Function for registering new Bin users
    def post(self, request):
        
        serializedUserData = UserSerializer(data=request.data)
## get assignedBin and check if it exist in User table, if it exist Throw error else Assign the bin to the user
        if serializedUserData.is_valid(raise_exception=True):
            assignedBin = serializedUserData.validated_data['assignedBin']
            bin_info = User.objects.filter(assignedBin=assignedBin).first()
            print(bin_info)
            if bin_info is None:
                serializedUserData.save()
                return Response(serializedUserData.data)
            
            response_data = {"Response": "Bin Already Assigned"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        return Response(serializedUserData.errors, status=status.HTTP_400_BAD_REQUEST)
    ######################Delete User#######################################
    def delete(self, request, pk):
        user = User.objects.filter(userId=pk).first()
        if user is None:
             response_data = {"response":"User does not exists"}
             return Response(response_data,status=status.HTTP_404_NOT_FOUND)
       #serializerData = UserSerializer(user)
        user.delete()
        response_data = {"response":"User Deleted"}
        return Response(response_data,status=status.HTTP_200_OK)

# Get registered User by ID
class UserDetailAPI(APIView):
    
    #Function to get a single registered user
    def get(self,request, pk):
        user = User.objects.filter(userId=pk)
        if len(user) < 1:
            print("echak")
            response_data = {"Response": "User does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        serializerUserData = UserSerializer(user, many=True)
        return Response(serializerUserData.data,status=status.HTTP_200_OK)
    
# Create your views here.
class BinAPI(APIView):
    
     #Function for registering new Bin users
    def post(self, request):
        print("wahala here")
        serializedBinData = BinSerializer(data=request.data)
        ## get bin binUniqueId and check if it exist in Bin table, if it exist Throw error else add/register the bin
        #print(binUniqueId)
        if serializedBinData.is_valid(raise_exception=True):
            binUniqueId = serializedBinData.validated_data['binUniqueId']
            bin_info = Bin.objects.filter(binUniqueId=binUniqueId).first()
            print(bin_info)
            if bin_info is None:
                serializedBinData.save()
                return Response(serializedBinData.data)
                
            #print(binUniqueId)
            response_data = {"Response": "Bin Unique_Id Already Exist"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
            
        return Response(serializedBinData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Function to get all registered users
    def get(self,request):
        bins = Bin.objects.all() 
        serializedBinData = BinSerializer(bins, many=True)
        return Response(serializedBinData.data)
    
    ######################Delete Bin#######################################
    def delete(self, pk):
        bin = Bin.objects.filter(binId=pk).first()
        if bin is None:
             response_data = {"response":"Bin does not exists"}
             return Response(response_data,status=status.HTTP_404_NOT_FOUND)
       #serializerData = UserSerializer(user)
        bin.delete()
        response_data = {"response":"Bin Deleted"}
        return Response(response_data,status=status.HTTP_200_OK)
    
    
# Create your views here.
class BinDataAPI(APIView):
    
    #Function to get all registered users
    def get(self,request):
        bin_para = BinData.objects.all() 
        serializerBinParaData = BinDataSerializer(bin_para, many=True)
        return Response(serializerBinParaData.data)
    
    
    #Function for registering new Bin users
    def post(self, request):
        print("wahala")
        serializerBinParaData = BinDataSerializer(data=request.data)
        if serializerBinParaData.is_valid(raise_exception=True):
            serializerBinParaData.save()
            return Response(serializerBinParaData.data)
        return Response(serializerBinParaData.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Get registered User by ID
class BinParametersAPI(APIView):
    
    #Function to get a single registered user
    def get(self,request, pk):
        _bin_para = BinData.objects.filter(_bin=pk)
        print(_bin_para)
        if len(_bin_para) < 1:
            print("echak")
            response_data = {"Response": "Bin details does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        serializerBinParaData = BinDataSerializer(_bin_para, many=True)
        return Response(serializerBinParaData.data,status=status.HTTP_200_OK)