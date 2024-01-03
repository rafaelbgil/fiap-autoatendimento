from src.entities.Pedido import Pedido
from .interfaces.PedidoRepositoryInterface import PedidoRepositoryInterface

class UseCasePedido:
    def obterListaPedidos(repositorio_pedido: PedidoRepositoryInterface) -> list[Pedido]:
        return repositorio_pedido.listPedido()
    
    def criarPedidoFromDict(repositorio_pedido: PedidoRepositoryInterface, dicionario_pedido: dict) -> dict:
        return repositorio_pedido.addPedidoFromDict(dicionario_pedido=dicionario_pedido)