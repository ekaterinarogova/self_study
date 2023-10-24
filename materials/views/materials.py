from rest_framework import generics

from materials.models import Materials
from materials.permissions import IsStaff
from materials.serializers import MaterialsSerializers


class MaterialsCreateAPIView(generics.CreateAPIView):
    """Creates an object of :model:`materials.Materials`"""
    serializer_class = MaterialsSerializers
    permission_classes = [IsStaff]


class MaterialsListAPIView(generics.ListAPIView):
    """Views a list of objects of :model:`materials.Materials` in the same section"""
    serializer_class = MaterialsSerializers

    def get_queryset(self):
        section = self.kwargs.get('pk')
        queryset = Materials.objects.filter(section=section)
        return queryset


class MaterialsRetrieveAPIView(generics.RetrieveAPIView):
    """Views one object of :model:`materials.Materials`"""
    serializer_class = MaterialsSerializers
    queryset = Materials.objects.all()


class MaterialsUpdateAPIView(generics.UpdateAPIView):
    """Updates an object of :model:`materials.Materials`"""
    serializer_class = MaterialsSerializers
    queryset = Materials.objects.all()
    permission_classes = [IsStaff]


class MaterialsDeleteAPIView(generics.DestroyAPIView):
    """Deletes an object of :model:`materials.Materials`"""
    queryset = Materials.objects.all()
    permission_classes = [IsStaff]
