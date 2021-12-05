from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView


class ClassificationTextAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'data': []})

    def post(self, request, *args, **kwargs):
        return Response({'data_p': []})
