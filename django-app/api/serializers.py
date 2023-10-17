from rest_framework import serializers
from .models import Cliente, Categoria


class ClienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    uuid = serializers.UUIDField(read_only=True)
    nome = serializers.CharField(max_length=120)
    email = serializers.CharField(max_length=120)
    cpf = serializers.CharField(max_length=11, required=False)
   
    def create(self, validated_data):
        return Cliente.objects.create(**validated_data)
    

class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return Categoria.objects.create(**validated_data)
    
    
class ProdutoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=40)
    preco = serializers.FloatField()
    id_categoria = serializers.IntegerField(required=False)
    descricao = serializers.CharField(max_length=1024, required=False)
    imagem_url = serializers.CharField(max_length=1024, required=False)