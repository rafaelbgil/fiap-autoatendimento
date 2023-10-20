from src.ports.PedidoRepositoryInterface import PedidoRepositoryInterface
from src.domain.entities.Pedido import Pedido
from src.domain.entities.PedidoFactory import PedidoFactory
from api.models import Pedido as PedidoModel

class PedidoRepositoryOrm(PedidoRepositoryInterface):
    def listPedido() -> [Pedido]:
        pedidos_queryset = PedidoModel.objects.all()
        lista_pedidos = []

        if not pedidos_queryset:
            return lista_pedidos
        
        for pedido_orm in pedidos_queryset:
            pedido = PedidoFactory.fromDict(dicionario_pedido=pedido_orm.__dict__)
            pedido.numero = pedido.id
            lista_pedidos.append(pedido)
        
        return lista_pedidos
