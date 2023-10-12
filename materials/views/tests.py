from rest_framework import generics
from rest_framework.response import Response

from materials.serializers import *


class TestsCreateAPIView(generics.CreateAPIView):
    serializer_class = TestsSerializers


class TestsListAPIView(generics.ListAPIView):
    serializer_class = TestsForUserSerializers

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


class TestAnswerView(generics.GenericAPIView):
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
