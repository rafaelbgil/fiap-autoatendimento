from .Produto import Produto
from abc import ABC


class Pedido(ABC):
    id: int | None
    cpf: str | None
    numero: int | None
    lista_itens: list | None
    valor: float

    def __init__(self, numero: int, valor: float, lista_itens: list | None = None, cpf: str | None = None, id: int = None):
        self.numero = numero
        self.cpf = cpf
        self.lista_itens = lista_itens
        self.valor = float(valor)
        self.id = id
