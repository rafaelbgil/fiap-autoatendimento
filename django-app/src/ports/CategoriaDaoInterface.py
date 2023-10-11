from abc import ABC, abstractmethod
from src.domain.entities.Categoria import Categoria

class CategoriaDaoInterface(ABC):
    @staticmethod
    def getCategoria(self, id: int) -> Categoria:
        pass

    @staticmethod
    def deleteCategoria(self, id: int):
        pass

    @staticmethod
    def addCategoria(self, categoria: Categoria):
        pass

    @staticmethod 
    def listCategoria(self) -> list[Categoria]:
        pass