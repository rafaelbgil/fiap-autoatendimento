from django.shortcuts import render, HttpResponse
from src.domain.entities.Pedido import Pedido
from rest_framework.decorators import api_view
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def cliente(request):
    """
    Api cliente
    """
    if request.method == 'GET':
        """
        parametros: teste
        """
        print('passou')
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)