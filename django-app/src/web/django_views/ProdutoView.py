from src.entities.ProdutoFactory import ProdutoFactory
from src.db.django_orm.ProdutoDaoOrm import ProdutoDaoOrm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes, extend_schema_view
from api.serializers import ProdutoSerializer

class ProdutoView(APIView):
    serializer_class = ProdutoSerializer
    """
    Api para gerencimamento de produtos
    """
    @extend_schema(responses=ProdutoSerializer(many=True), summary='Obtém lista de produtos')
    def get(self, request, format=None):
        """
        Api para obter lista de **produtos**
        """
        produtos = ProdutoDaoOrm().listProduto()
        serializer = ProdutoSerializer(instance=produtos, many=True)
        #serializer.is_valid()
        return Response(serializer.data)
    
    @extend_schema(summary='Adiciona novo produto')
    def post(self, request, format=None):
        """
        Api para cadastrar **produto**
        """
        try:
            produto = ProdutoDaoOrm().addProduto(ProdutoFactory.fromDict(dicionario_produto=request.data))
        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        return Response(produto.toDict(), status=status.HTTP_201_CREATED)
        
