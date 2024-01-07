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
    Api para atualizar status do pedido via webhook
    """
    serializer_class = PedidoSerializer

    def post(self, request, format=None):
        """
        Adiciona novo **pedido**
        """
        pedido = PedidoRepositoryOrm.addPedidoFromDict(
            dicionario_pedido=request.data)
        serializer = PedidoSerializer(instance=pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)