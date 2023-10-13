from src.ports.CategoriaDaoInterface import CategoriaDaoInterface
from src.domain.entities.Categoria import Categoria
from src.domain.entities.CategoriaFactory import CategoriaFactory
from api.models import Categoria as CategoriaModel


class CategoriaDaoOrm(CategoriaDaoInterface):
    def getCategoria(self, id: str) -> Categoria:
        if not id.isnumeric():
            raise Exception('Código de categoria inválido, favor informar um número.')
        try:
            categoria_queryset = CategoriaModel.objects.get(id=id)
        except:
            raise Exception('Categoria não encontrada.')

        return CategoriaFactory.fromDict(categoria_queryset.__dict__)

    def listCategoria(self) -> list[Categoria]:
        categorias_queryset = CategoriaModel.objects.all()
        categorias = []
        for categoria in categorias_queryset.iterator():
            categorias.append(CategoriaFactory.fromDict(
                dicionario_categoria=categoria.__dict__))

        return categorias

    def deleteCategoria(self):
        pass

    def addCategoria(self, categoria: Categoria):
        categoria_orm = CategoriaModel()
        for atributo in categoria.__dict__.keys():
            if categoria.__dict__[atributo] and categoria.__dict__[atributo] != 'None':
                categoria_orm.__setattr__(
                    __name=atributo, __value=categoria.__dict__[atributo])
        try:
            categoria_orm.save()
        except:
            raise Exception('Não foi possível adicionar a categoria.')

        categoria.id = categoria_orm.id
        return categoria
