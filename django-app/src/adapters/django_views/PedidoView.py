from src.domain.entities.PedidoFactory import PedidoFactory
from src.adapters.django_orm.PedidoRepositoryOrm import PedidoRepositoryInterface
from rest_framework.views import APIView
from api.models import Pedido as PedidoModel
from api.serializers import PedidoSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes


class PedidoView(APIView):
    """
    Api para gerencimento de pedidos
    """
    serializer_class = PedidoSerializer

    @extend_schema(summary='Obtém lista de pedidos', examples=[
        OpenApiExample('Exemplo de pedido', value={
            "id": 1,
            "cpf": "12345678901",
            "valor": 10.90,
            "status": "aguardando_pagamento",
            "lista_produtos": [
                {
                    "id": 1,
                    "nome": "Hamburguer",
                    "preco": 10.90,
                    "imagem_url": 'hamburger.png',
                    "quantidade": 1
                }
            ]
        }, response_only=True)
    ])
    def get(self, request, format=None):
        pedidos = PedidoModel.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)

        return Response(serializer.data)

    @extend_schema(summary='Adiciona novo pedido', examples=[
        OpenApiExample('Exemplo de pedido', value={
            "cpf": "12345678901",
            "lista_produtos": [
                {
                    "id": 1,
                    "quantidade": 1
                }
            ]
        }, request_only=True),
        OpenApiExample('Exemplo de pedido', value={
            "id": 1,
            "cpf": "12345678901",
            "valor": 10.90,
            "status": "aguardando_pagamento",
            "lista_produtos": [
                {
                    "id": 1,
                    "nome": "Hamburguer",
                    "preco": 10.90,
                    "imagem_url": 'hamburger.png',
                    "quantidade": 1
                }
            ]
        }, response_only=True)
    ])
    def post(self, request, format=None):
        pass
