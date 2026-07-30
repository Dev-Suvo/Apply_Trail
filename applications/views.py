from django.shortcuts import render

from .serializers import Applicationserializers
from .models import Application
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(["GET","POST"])
def application_list(request):
    if request.method == "GET":
        apllications = Application.objects.all()
        serializer = Applicationserializers(apllications, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = Applicationserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)