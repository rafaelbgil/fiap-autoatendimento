from abc import ABC, abstractmethod
from src.entities.Produto import Produto

class ProdutoDaoInterface(ABC):
    @abstractmethod
    def getProduto(self, id : int) -> Produto:
        pass

    @abstractmethod
    def listProdutoByCategoria() -> list[Produto]:
        pass
    
    @abstractmethod
    def listProduto(self)-> [Produto]:
        pass

    @abstractmethod
    def deleteProduto(self, id: int):
        pass

    @abstractmethod
    def addProduto(self, produto: Produto) -> bool:
        pass

    @abstractmethod
    def updateProduto(self, produto: Produto) -> Produto:
        pass
    
