from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from market.models import Order
from market.serializers.order import CreateOrderSerializer, OrderSerializer
from market.serializers.user import UserSerializer


class CreateOrder(APIView):
  queryset = Order.objects.all()
  permission_classes = [permissions.IsAuthenticated]
  def post(self, request, *args, **kwargs):
    request.data['user'] = request.user.id
    serializer = CreateOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, *args, **kwargs):
    request.data['user'] = request.user.id
    obj = Order.objects.get(id = request.data['id'])
    obj.status = request.data['status']
    obj.save()
    serializer = CreateOrderSerializer(instance=Order.objects.get(id = request.data['id']), data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderList(generics.ListAPIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = OrderSerializer
  def get_queryset(self):
      return Order.objects.filter(user = self.request.user.id)
