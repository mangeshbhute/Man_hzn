from django.contrib import admin
from .models import Prodect_Details

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['no','name','quan','buyer']

admin.site.register(Prodect_Details,ProductAdmin)