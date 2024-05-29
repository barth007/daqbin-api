from django.db import models, transaction
from django_countries.fields import CountryField
from  django.db.models.signals import post_save
from django.dispatch import receiver
from sqlite3 import IntegrityError



BIN_SIZE_TYPE = (
     ("small", "Small"),
     ("medium", "Medium"),
     ("large", "Large")
)


class Bin(models.Model):
    bin_unique_id = models.CharField(max_length=10, unique=True,  editable=False)
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
        if not self.bin_unique_id:
            while True:
                try:
                    with transaction.atomic():
                        max_bin_id = Bin.objects.all().aggregate(models.Max('id'))['id__max']
                        if max_bin_id is None:
                            max_bin_id = 1 
                        else:
                            max_bin_id += 1
                        self.bin_unique_id = f"BIN{str(max_bin_id).zfill(4)}"
                        super().save(*args, **kwargs)
                        break
                except IntegrityError:
                    continue
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.bin_unique_id


    class Meta:
        ordering = ["bin_unique_id"]
    
    
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bin_id = models.OneToOneField(Bin, on_delete=models.CASCADE, related_name="bin_id")
   
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UserAddress(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_id")
    house_no = models.CharField(max_length=100)
    street = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    country = CountryField()

    def __str__(self):
        return f"{self.house_no}, {self.street},{self.city}, {self.country.name}."
    
    
class BinData(models.Model):
    the_bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name="the_bin")
    bin_level = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    bin_temperaure = models.CharField(max_length=20)
    bin_orientation = models.CharField(max_length=20)
    battery_level = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.the_bin.bin_unique_id
    

@receiver(post_save, sender=User)
def create_assign_bin(sender, created, instance, **kwargs):
    if created:
        try:
            with transaction.atomic():
                bin_obj = Bin.objects.select_for_update().get(pk=instance.bin_id.id)
                bin_obj.is_bin_asigned = True
                bin_obj.save()
        except IntegrityError as e:
            print(f"An integrity error occurred: {e}")
        