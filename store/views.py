from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from .models import Product
from .serializers import ProductSerializer
 
# Create your views here.
# def product_list(request):
#     return HttpResponse('ok')
@api_view()
def product_list(request):
    queryset = Product.objects.all()
    Serializer = ProductSerializer(queryset,many=True)
    return Response(Serializer.data)
# Error handler 
# @api_view()
# def product_detail(request,id):
#     try:
#         product = Product.objects.get(pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# better error handler 
@api_view()
def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)