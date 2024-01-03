from src.entities.Categoria import Categoria
from .interfaces.CategoriaDaoInterface import CategoriaDaoInterface

class UseCaseCategoria:
    def obterListaCategoria(repository_categoria: CategoriaDaoInterface) -> list[Categoria]:
        return repository_categoria.listCategoria()
    
    def obterCategoria(repository_categoria: CategoriaDaoInterface, id: int) -> Categoria:
        return repository_categoria.getCategoria(id=id)
    
   