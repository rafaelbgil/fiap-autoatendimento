from abc import ABC, abstractmethod
from src.entities.Pedido import Pedido

class PedidoRepositoryInterface(ABC):
    @staticmethod
    def getPedido(self, id: int) -> Pedido:
        pass
    
    @staticmethod
    def listPedido(self) -> list[Pedido]:
        pass
    
    @staticmethod
    def addPedido(self, pedido: Pedido) -> Pedido:
        pass

    @staticmethod
    def addPedidoFromDict( dicionario_pedido: dict) -> dict:
        pass