from django.db.models.query import QuerySet
from django.shortcuts import render ,get_object_or_404
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from Coders.serializers import ClientSerializer,ProjectSerializer
from Coders.models import Client, Project
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class clientList(APIView):

    def get(self, request):
        Clients = Client.objects.all()
        serializer = ClientSerializer(Clients, many = True)
        return Response(serializer.data)

class Createclient(APIView):


    def post(self, request):
        serializer= ClientSerializer(data= request.data )
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)



    def put(self, request):
        client_object= Client.objects.get()
        data = request.data

        client_object.client_name= data["client_name"]
        client_object.created_by= data["created_by"]
        client_object.created_at= data["created_at"]
        client_object.Project= data["Project"]

        client_object.save()

        serializer= ClientSerializer(data)

        return Response(serializer.data)

        

        










