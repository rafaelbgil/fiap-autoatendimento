class Categoria:
    id: int
    nome: str

    def __init__(self, nome=None, id=None):
        self.nome = nome
        self.id = id
    
    def toDict(self):
        return ({
            'id' : self.id,
            'nome' : self.nome
        })