from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import TextClassificationSerializer
from ..dt_corporate_course import settings
from ..dt_corporate_course.nlp_microservice.text_classification import predict


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

        data_predict = predict(settings.MODEL_NLP, request.data['data'])
        return Response({'initial_data': request.data['data'], 'predict': data_predict})
