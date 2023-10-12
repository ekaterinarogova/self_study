from rest_framework import generics

from materials.serializers import *


class SectionCreateAPIView(generics.CreateAPIView):
    serializer_class = SectionSerializers


class SectionListAPIView(generics.ListAPIView):
    serializer_class = SectionSerializers
    queryset = Section.objects.all()


class SectionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SectionDetailViewSerializers
    queryset = Section.objects.all()


class SectionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SectionSerializers
    queryset = Section.objects.all()


class SectionDeleteAPIView(generics.DestroyAPIView):
    queryset = Section.objects.all()