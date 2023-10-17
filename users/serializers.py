from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for :model:`users.User` """
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email',)
        