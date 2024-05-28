from django.db import models
from django_countries.fields import CountryField


BIN_SIZE_TYPE = (
     ("small", "Small"),
     ("medium", "Medium"),
     ("large", "Large")
)


class Bin(models.Model):
    bin_unique_id = models.CharField(max_length=10, unique=True, editable=False, default="BIN0000")
    bin_size = models.CharField(choices=BIN_SIZE_TYPE,  max_length=10, default="small")
    manufacture_date = models.DateField(auto_now_add=True)
    is_bin_asigned = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        """
        overriding the save method

        Args:
            *args: positional arguments
            **Kwargs: key arguments
        """
        if not self.pk: #only generate if it's a new object
            max_bin_str = Bin.objects.aggregate(largest=models.Max('bin_unique_id'))['largest'] or 0
            if max_bin_str:
                max_bin_id = int(max_bin_str[3:]) + 1 
            self.bin_unique_id = f"BIN{str(max_bin_id).zfill(4)}"
        super(Bin, self).save(*args, **kwargs)
    def __str__(self):
        return self.bin_unique_id
    class Meta:
        ordering = ["bin_unique_id"]
    
    
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bin_id = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name="bin_id")
   
    
    def __str__(self):
        return self.first_name

class UserAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    house_no = models.CharField(max_length=100)
    street = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    country = CountryField()

    def __str__(self):
        return f"{self.house_no}, {self.street},{self.city}, {self.country}."
    
    
class BinData(models.Model):
    the_bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name="the_bin")
    bin_level = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    bin_temperaure = models.CharField(max_length=20)
    bin_orientation = models.CharField(max_length=20)
    battery_level = models.CharField(max_length=10)
    
    def __str__(self):
        return self.the_bin.bin_unique_id
    