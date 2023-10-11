from .Item import Item
from abc import ABC

class Pedido(ABC):
    cpf : str | None
    numero : int
    lista_itens : list[Item]
    valor : float

    def __init__(self, numero: int, lista_itens: list[Item], valor: float, cpf: str | None ):
        self.numero = int(numero)
        self.cpf = cpf
        self.lista_itens = lista_itens
        self.valor = float(valor)

    