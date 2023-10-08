from ddd.domain.entities.ClienteFactory import ClienteFactory
from ddd.domain.entities.CategoriaFactory import CategoriaFactory
from rest_framework.views import APIView
from .models import Cliente, Categoria
from .serializers import ClienteSerializer, CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter


class ClienteView(APIView):
    """
    Api para gerenciamento de clientes
    """
    serializer_class = ClienteSerializer

    @extend_schema(responses=ClienteSerializer(many=True))
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
        try:
            ClienteFactory.fromDict(request.data)
        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ClienteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 'erro', 'detalhes': serializer._errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)


class ClienteDetalhesView(APIView):
    serializer_class = ClienteSerializer

    def get(self, request, uuid: str, format=None):
        """
        Visualiza dados de usuario selecionado
        """
        try:
            cliente_objeto = ClienteFactory.fromDict(
                dicionario_cliente={'uuid': uuid})
        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cliente = Cliente.objects.get(uuid=cliente_objeto.uuid)
        except:
            return Response(data={'status': 'erro', 'detalhes': "Cliente não encontrado, verifique o uuid"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClienteSerializer(instance=cliente)

        return Response(data=serializer.data)


class CategoriaView(APIView):
    serializer_class = CategoriaSerializer

    @extend_schema(responses=CategoriaSerializer(many=True), description='Api para inclusao de algo')
    def get(self, request, format=None):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(data=categorias, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            CategoriaFactory.fromDict(request.data)
        except Exception as erro:
            return Response({'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CategoriaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 'erro', 'detalhes': serializer._errors}, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer.save()
        except Exception as erro:
            return Response({'status': 'erro', 'detalhes': 'Não foi possível cadastrar a nova categoria.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data)


class CategoriaDetalhesView(APIView):
    serializer_class = CategoriaSerializer

    def delete(self, request, id: int, format=None):
        try:
            categoria = Categoria.objects.get(id=id)
        except: 
            return Response(data={'status' : 'erro', 'detalhes' : 'Categoria nao encontrada.'}, status=status.HTTP_400_BAD_REQUEST)    

        try:    
            categoria.delete()
            return Response(data={'status' : 'sucesso', 'detalhes' : 'Categoria removida com sucesso.'}, status=status.HTTP_200_OK)
        except:
            return Response(data={'status' : 'erro', 'detalhes' : 'Não foi possível remover a categoria'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
            