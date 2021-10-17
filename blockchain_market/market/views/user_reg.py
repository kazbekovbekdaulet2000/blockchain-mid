from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from market.serializers.user import UserSerializer

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    # model = get_user_model()
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny ]
    serializer_class = UserSerializer