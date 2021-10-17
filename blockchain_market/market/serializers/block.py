from ..models import BlockChain
from rest_framework import serializers

class BlockChainSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlockChain
    fields = '__all__'