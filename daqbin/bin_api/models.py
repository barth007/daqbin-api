from django.db import models

# Create your models here.

## Bin model for adding manufacture Bins ##
class Bin(models.Model):
    binId = models.AutoField(primary_key=True)
    binUniqueId = models.CharField(max_length=10)
    binSize = models.CharField(max_length=10)
    manufactureDate = models.DateField(blank=True)
    
    def __str__(self):
        return self.binUniqueId
    
    
## User Model for Registering Bin owners/users ##    
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    assignedBin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.firstName
    
    
## BinData model for posting Bins parameters ##
class BinData(models.Model):
    binDataId = models.AutoField(primary_key=True)
    _bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    #accessKey = models.CharField(max_length=20)
    binLevel = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    binTemperaure = models.CharField(max_length=20)
    binOrientation = models.CharField(max_length=20)
    batteryLevel = models.CharField(max_length=10)
    
    def __str__(self):
        return self._bin.binUniqueId
    