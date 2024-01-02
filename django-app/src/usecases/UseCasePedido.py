from src.entities.Pedido import Pedido
from .interfaces.PedidoRepositoryInterface import PedidoRepositoryInterface

class UseCasePedido:
    def getListaPedidos(repositorio_pedido: PedidoRepositoryInterface) -> list[Pedido]:
        return repositorio_pedido.listPedido()
    
    def addPedido(repositorio_pedido: PedidoRepositoryInterface) -> Pedido:
        pass