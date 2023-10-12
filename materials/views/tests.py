from rest_framework import generics

from materials.serializers import *


class TestsCreateAPIView(generics.CreateAPIView):
    serializer_class = TestsSerializers


class TestsListAPIView(generics.ListAPIView):
    serializer_class = TestsSerializers

    def get_queryset(self):
        materials = self.kwargs.get('pk')
        queryset = Tests.objects.filter(materials=materials)
        return queryset


class TestsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TestsForUserSerializers
    queryset = Tests.objects.all()


class TestsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TestsForUserSerializers
    queryset = Tests.objects.all()


class TestsDeleteAPIView(generics.DestroyAPIView):
    queryset = Tests.objects.all()
