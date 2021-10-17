from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
    write_only_fields = ('password',)
    read_only_fields = ('id',)

  def validate(self, attrs):
    return super().validate(attrs)

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )

    user.set_password(validated_data['password'])
    user.save()

    return user