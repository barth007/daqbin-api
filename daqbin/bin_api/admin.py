from django.contrib import admin
from .models import Bin, User, BinData, UserAddress

# Register your models here.
admin.site.register(Bin)
admin.site.register(User)
admin.site.register(BinData)
admin.site.register(UserAddress)

