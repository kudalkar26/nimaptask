from django.db import models
from rest_framework import serializers
from Coders.models import Client
from Coders.models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','Project']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name','created_by','created_at', 'Project','Project']