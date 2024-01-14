from .Cobranca import Cobranca
from .validators import  _validarUuid

class CobrancaFactory:
    @staticmethod
    def createCobranca(status: str, fornecedor_meio_pagto: str,codigo: str = None ,pix_codigo: str = None) -> Cobranca:
        _validarUuid(uuid=codigo)
        return Cobranca(codigo=codigo, status=status,fornecedor_meio_pagto=fornecedor_meio_pagto,pix_codigo=pix_codigo)