from django.shortcuts import render, HttpResponse
from ddd.domain.entities.ClienteFactory  import ClienteFactory
from rest_framework.views import APIView
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
import json


class ClienteList(APIView):
    """
    Api para gerenciamento de clientes
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

   
    def get(self, request, format=None):
        """
        Visualiza os usuarios cadastrados
        """
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(data=clientes, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    
    def post(self, request, format=None):
        """
        Cadastra novo usuario
        """
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid()
        try:
            cliente = ClienteFactory.fromDict(serializer.data)
        except:
            return Response(data={'status' : 'Erro', 'motivo' : 'E-mail inválido'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.create(serializer.data)
        return Response(serializer.data)

    