from abc import ABC, abstractmethod
from src.entities.Categoria import Categoria

class CategoriaDaoInterface(ABC):
    @staticmethod
    def getCategoria(self, id: int) -> Categoria:
        pass

    @staticmethod
    def deleteCategoria(self, id: int) -> bool:
        pass

    @staticmethod
    def addCategoria(self, categoria: Categoria):
        pass

    @staticmethod 
    def listCategoria() -> list[Categoria]:
        pass