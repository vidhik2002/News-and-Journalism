from django.shortcuts import render

# Create your views here.

from .serializers import (
    mySerializer
)
from .models import (
    Article
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import FormParser,MultiPartParser

class myAPI(APIView):
    parser_classes = [FormParser,MultiPartParser]
    def get(self, request):
        serializer_object = Article.objects.all()
        serializer = mySerializer(serializer_object, many=True)
        return Response(serializer.data, status=200)


    def post(self, request):
        serializer = mySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({'error': serializer.errors}, status=401)

