from rest_framework.views import APIView
from api.models import Categoria
from src.adapters.django_orm.CategoriaDaoOrm import CategoriaDaoOrm
from api.serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiExample

class CategoriaDetalhesView(APIView):
    serializer_class = CategoriaSerializer

    @extend_schema(summary='Obtém dados de categoria selecionada', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id": 1,
                              "nome": "salgados"},
                       request_only=False,
                       response_only=True,
                       )
    ])
    def get(self, request, id: int, format=None):
        """
        Obtém dados de categoria selecionada
        """
        try:
            categoria = CategoriaDaoOrm().getCategoria(id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategoriaSerializer(instance=categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(summary='Remove categoria selecionada')
    def delete(self, request, id: int, format=None):
        """
        Remove categoria selecionada
        """
        try:
            categoria = Categoria.objects.get(id=id)
        except:
            return Response(data={'status': 'erro', 'detalhes': 'Categoria nao encontrada.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            categoria.delete()
            return Response(data={'status': 'sucesso', 'detalhes': 'Categoria removida com sucesso.'}, status=status.HTTP_200_OK)
        except:
            return Response(data={'status': 'erro', 'detalhes': 'Não foi possível remover a categoria'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
