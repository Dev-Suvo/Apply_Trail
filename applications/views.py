from django.shortcuts import render

from .serializers import Applicationserializers
from .models import Application
from rest_framework.response import Response
from rest_framework import status

from rest_framework .views import APIView


from rest_framework .viewsets import ModelViewSet

class JobApplication(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = Applicationserializers

