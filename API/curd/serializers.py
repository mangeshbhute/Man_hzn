from rest_framework import serializers

from .models import Prodect_Details

class ProductDetailsSer(serializers.ModelSerializer):
    class Meta:
        model=Prodect_Details
        fields="__all__"