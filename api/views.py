from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import TextClassificationSerializer


class ClassificationTextAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'data': []})

    @staticmethod
    def get_serializer_text_classification(data):
        if len(data) > 1:
            text_ser = TextClassificationSerializer(data=data, many=True)
        else:
            text_ser = TextClassificationSerializer(data=data)
        return text_ser

    def post(self, request, *args, **kwargs):
        if 'data' not in request.data:
            return Response({'error': 'Invalid data or key'}, status=status.HTTP_400_BAD_REQUEST)

        text_ser = ClassificationTextAPIView.get_serializer_text_classification(request.data['data'])

        if text_ser.is_valid(raise_exception=True):
            text_ser.save()

        return Response({'data_p': []})
