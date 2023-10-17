from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Creates an object of :model:`users.User`"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
