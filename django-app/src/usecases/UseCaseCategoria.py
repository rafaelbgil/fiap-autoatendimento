from src.entities.Categoria import Categoria
from .interfaces.CategoriaDaoInterface import CategoriaDaoInterface

class UseCaseCategoria:
    def getListaCategoria(repository_categoria: CategoriaDaoInterface) -> list[Categoria]:
        return repository_categoria.listCategoria()
    