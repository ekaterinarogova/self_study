from rest_framework import generics

from materials.models import Section
from materials.permissions import IsStaff
from materials.serializers import SectionSerializers, SectionDetailViewSerializers


class SectionCreateAPIView(generics.CreateAPIView):
    """Creates an object of :model:`materials.Section`"""
    serializer_class = SectionSerializers
    permission_classes = [IsStaff]


class SectionListAPIView(generics.ListAPIView):
    """Views a list of objects of :model:`materials.Section`"""
    serializer_class = SectionSerializers
    queryset = Section.objects.all()


class SectionRetrieveAPIView(generics.RetrieveAPIView):
    """Views one object of :model:`materials.Section` with all the materials"""
    serializer_class = SectionDetailViewSerializers
    queryset = Section.objects.all()


class SectionUpdateAPIView(generics.UpdateAPIView):
    """Updates an object of :model:`materials.Section`"""
    serializer_class = SectionSerializers
    queryset = Section.objects.all()
    permission_classes = [IsStaff]


class SectionDeleteAPIView(generics.DestroyAPIView):
    """Deletes an object of :model:`materials.Section`"""
    queryset = Section.objects.all()
    permission_classes = [IsStaff]
