from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    uuid = serializers.CharField(max_length=32)
    nome = serializers.CharField(max_length=120)
    email = serializers.CharField(max_length=120)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Cliente.objects.create(**validated_data)