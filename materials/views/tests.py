from rest_framework import generics
from rest_framework.response import Response

from materials.permissions import IsStaff
from materials.serializers import *


class TestsCreateAPIView(generics.CreateAPIView):
    """Creates an object of :model:`materials.Tests`"""
    serializer_class = TestsSerializers
    permission_classes = [IsStaff]


class TestsListAPIView(generics.ListAPIView):
    """Views a list of object of :model:`materials.Tests` for the following material"""
    serializer_class = TestsForUserSerializers

    def get_queryset(self):
        materials = self.kwargs.get('pk')
        queryset = Tests.objects.filter(materials=materials)
        return queryset


class TestsRetrieveAPIView(generics.RetrieveAPIView):
    """Views one object of :model:`materials.Tests`"""
    serializer_class = TestsForUserSerializers
    queryset = Tests.objects.all()


class TestsUpdateAPIView(generics.UpdateAPIView):
    """Updates an object of :model:`materials.Tests`"""
    serializer_class = TestsForUserSerializers
    queryset = Tests.objects.all()
    permission_classes = [IsStaff]


class TestsDeleteAPIView(generics.DestroyAPIView):
    """Deletes an object of :model:`materials.Tests`"""
    queryset = Tests.objects.all()
    permission_classes = [IsStaff]


class TestAnswerView(generics.GenericAPIView):
    """Verifies user's answer for object of :model:`materials.Tests`"""
    queryset = Tests.objects.all()
    serializer_class = TestsSerializers

    def post(self, request, *args, **kwargs):
        test = self.get_object()
        user_answer = request.data.get('answer')

        if user_answer.lower() == test.correct_answer.lower():
            response_data = {'result': 'correct'}
        else:
            response_data = {'result': 'incorrect',
                             'correct_answer': test.correct_answer}

        return Response(response_data)
