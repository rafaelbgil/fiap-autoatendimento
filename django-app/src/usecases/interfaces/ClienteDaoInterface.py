from abc import ABC, abstractmethod
from src.entities.Cliente import Cliente

class ClienteDaoInterface(ABC):
    @abstractmethod
    def getCliente(self, uuid: str) -> Cliente:
        pass
    
    @abstractmethod
    def deleteCliente(self, uuid: str):
        pass

    @abstractmethod
    def listCliente(self) -> list[Cliente]:
        pass

    @abstractmethod
    def addCliente(self, cliente: Cliente):
        pass