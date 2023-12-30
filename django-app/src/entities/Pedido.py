from .Produto import Produto
from abc import ABC


class Pedido(ABC):
    id: int | None
    status: str
    cpf: str | None
    numero: int | None
    lista_itens: list | None
    valor: float

    def __init__(self, numero: int, valor: float, status: str = 'aguardando_pagamento', lista_itens: list | None = None, cpf: str | None = None, id: int = None):
        self.numero = numero
        self.status = status
        self.cpf = cpf
        self.lista_itens = lista_itens
        self.valor = float(valor)
        self.id = id
