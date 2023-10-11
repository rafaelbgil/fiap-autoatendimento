from src.domain.entities.CategoriaFactory import CategoriaFactory
from rest_framework.views import APIView
from api.models import Categoria
from api.serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


class CategoriaView(APIView):
    serializer_class = CategoriaSerializer

    @extend_schema(responses=CategoriaSerializer(many=True), summary='Obtém lista de categorias')
    def get(self, request, format=None):
        """
        Api para listar categorias
        """
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(data=categorias, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(summary='Adiciona nova categoria')
    def post(self, request, format=None):
        """
        Api para adicionar categoria
        """
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

        return Response(serializer.data, status=status.HTTP_201_CREATED)
