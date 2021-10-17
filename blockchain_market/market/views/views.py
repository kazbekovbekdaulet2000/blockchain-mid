from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from market.blockchain import Blockchain
from market.models import BlockChain, Product_coffee
from rest_framework import status
from rest_framework.views import APIView
from market.serializers.block import BlockChainSerializer

from market.serializers.product_ser import ProductSerilizer
# Create your views here.

blockchain = Blockchain()

class ProductView(generics.ListAPIView):
  queryset = Product_coffee.objects.all()
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ProductSerilizer


class AllBlocks(generics.ListAPIView):
  queryset = BlockChain.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = BlockChainSerializer


class CreatBlock(APIView):
  queryset = BlockChain.objects.all()
  def post(self, request, *args, **kwargs):
    serializer = BlockChainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
