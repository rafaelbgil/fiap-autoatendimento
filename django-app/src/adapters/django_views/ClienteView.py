from src.domain.entities.ClienteFactory import ClienteFactory
from src.adapters.django_orm.ClienteDaoOrm import ClienteDaoOrm
from rest_framework.views import APIView
from api.serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes


class ClienteView(APIView):
    """
    Api para gerenciamento de clientes
    """
    serializer_class = ClienteSerializer

    @extend_schema(responses=ClienteSerializer(many=True), summary='Obtém lista de clientes cadastrados')
    def get(self, request, format=None):
        """
        Retorna uma lista de **clientes**.
        """
        clientes = ClienteDaoOrm().listCliente()
        serializer = ClienteSerializer(data=clientes, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)


    @extend_schema(summary='Adiciona novo cliente', responses={201: ClienteSerializer, 401: None}, parameters=[
        OpenApiParameter(name='nome', type=type(str),
                         description='Nome completo do cliente',

                         examples=OpenApiExample(name='nome', value='Joao silva', description='Nome completo do cliente')),
        OpenApiParameter(name='email', type=type(str),
                         description='E-mail do cliente'),
        OpenApiParameter(name='cpf', type=type(str),
                         description='Cpf do cliente')

    ])
    def post(self, request, format=None):
        """
        Api para **cadastrar** cliente
        """
        try:
            cliente = ClienteDaoOrm().addCliente(ClienteFactory.fromDict(request.data))
        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        return Response(cliente.toDict(), status=status.HTTP_201_CREATED)
