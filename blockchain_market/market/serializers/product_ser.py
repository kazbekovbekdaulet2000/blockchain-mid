from rest_framework import serializers
from market.models import CoffeeType, Product_coffee

class CoffeeTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = CoffeeType 
    fields = "__all__"

class ProductSerilizer(serializers.ModelSerializer):
  type = CoffeeTypeSerializer(read_only = True)
  class Meta:
    model = Product_coffee 
    fields = "__all__"