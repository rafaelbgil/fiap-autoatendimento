import re

class Cliente():
    nome: str = None
    email: str = None
    uuid : str = None

    def __init__(self, nome, email, uuid):
        self.nome = nome
        self.email = email
        self.uuid = uuid

    