from django.contrib import admin
from .models import Bin, User, BinData

# Register your models here.
admin.site.register(Bin)
admin.site.register(User)
admin.site.register(BinData)

