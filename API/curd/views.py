from django.shortcuts import render
from .models import Prodect_Details
from .serializers import ProductDetailsSer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class ProductTable(APIView):
    def get(self,r):
        prd=Prodect_Details.objects.all()
        serobj=ProductDetailsSer(prd,many=True)
        return Response(serobj.data)
    def post(self,r):
        serobj=ProductDetailsSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_204_NO_CONTENT)
    def put(self,r,pk):
        prdobj=Prodect_Details.objects.get(pk=pk)
        serobj=ProductDetailsSer(prdobj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_200_OK)
        return Response(serobj.errors, status=status.HTTP_204_NO_CONTENT)
    def delete(self,r,pk):
        prdobj=Prodect_Details.objects.get(pk=pk)
        prdobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


