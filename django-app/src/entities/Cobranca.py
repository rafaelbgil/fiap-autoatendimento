from .validators import _validarUuid

class Cobranca:
    codigo: str = None
    status: str
    fornecedor_meio_pagto: str
    pix_codigo: str

    def __init__(self, codigo, status, fornecedor_meio_pagto, pix_codigo):
        self.codigo = codigo
        self.status = status
        self.fornecedor_meio_pagto = fornecedor_meio_pagto
        self.pix_codigo = pix_codigo

    def definirCodigo(self, codigo: str):
        if type(self.codigo) != None:
            raise Exception('Codigo ja definido, nao é possível alterar')
        if _validarUuid(codigo):
            self.codigo = codigo
        