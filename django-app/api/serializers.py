from rest_framework import serializers
from .models import Cliente, Categoria


class ClienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    uuid = serializers.CharField(max_length=32, read_only=True)
    nome = serializers.CharField(max_length=120)
    email = serializers.CharField(max_length=120)
   
    def create(self, validated_data):
        return Cliente.objects.create(**validated_data)
    

class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return Categoria.objects.create(**validated_data)
    
    