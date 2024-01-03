from src.db.django_orm.PedidoRepositoryOrm import PedidoRepositoryOrm
from src.usecases.UseCasePedido import UseCasePedido
from src.controllers.FormatPedido import FormatPedido

from api.serializers import PedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

class PedidoDetalhesView(APIView):
    """
    Api para obter informacoes do pedido selecionado
    """
    serializer_class = PedidoSerializer


    def get(self, request, id, format=None):
        """
        Obtém informacao de **pedido**
        """
        try:
            pedido = UseCasePedido.obterPedido(repositorio_pedido=PedidoRepositoryOrm,id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
        pedido_dict = FormatPedido.fromPedidoToDict(pedido)
        return Response(data=pedido_dict, status=status.HTTP_200_OK)
