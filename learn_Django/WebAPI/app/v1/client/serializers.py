from rest_framework import serializers
from app.models import Client ,Post
class ClientV1Serializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= ['id','name','gender','active','created_at']

class PostV1Serializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = '__all__'