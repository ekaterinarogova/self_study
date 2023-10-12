from rest_framework import generics

from materials.serializers import *


class MaterialsCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialsSerializers


class MaterialsListAPIView(generics.ListAPIView):
    serializer_class = MaterialsSerializers

    def get_queryset(self):
        section = self.kwargs.get('pk')
        queryset = Materials.objects.filter(section=section)
        return queryset


class MaterialsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialsSerializers
    queryset = Materials.objects.all()


class MaterialsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialsSerializers
    queryset = Materials.objects.all()


class MaterialsDeleteAPIView(generics.DestroyAPIView):
    queryset = Materials.objects.all()