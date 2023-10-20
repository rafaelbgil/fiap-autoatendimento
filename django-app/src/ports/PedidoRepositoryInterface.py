from abc import ABC, abstractmethod
from src.domain.entities.Pedido import Pedido

class PedidoRepositoryInterface(ABC):
    
    def getPedido(self, id: int) -> Pedido:
        pass

    def listPedido(self) -> [Pedido]:
        pass

    def addPedido(self, pedido: Pedido):
        pass