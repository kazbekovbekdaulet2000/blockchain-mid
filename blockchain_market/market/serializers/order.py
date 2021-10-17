from rest_framework import serializers, fields
from market.models import BlockChain, Order, Product_coffee
from django.contrib.auth import get_user_model
import json

from market.serializers.product_ser import ProductSerilizer
User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
  product = ProductSerilizer(read_only = True)
  class Meta:
    model = Order
    fields = "__all__"

  def update(self, instance, validated_data):
    instance.status = validated_data.get('status', instance.status)
    BlockChain.objects.create(data = instance)
    return instance

  def create(self, validated_data):
    print(validated_data['product'])
    product = Product_coffee.objects.get(id = validated_data['product'].id)
    validated_data['price'] = product.price * validated_data['entity']
    validated_data['weight'] = product.weight * validated_data['entity']
    product.entity = product.entity - validated_data['entity']
    product.save()
    order = super().create(validated_data)
    BlockChain.objects.create(data = order)
    return order 