from .Cliente import Cliente
import re
def _validarEmail(email) -> str:
        if not re.search('@', email):
            raise Exception('Email invalido')
        
        if not re.search('\.', email):
            raise Exception('Email invalido')
        
        if not re.match('^[a-z0-9][\w.-]*@[a-z0-9][\w.-]*[a-z0-9]$', email):
            raise Exception('Email invalido')
        return email

class ClienteFactory:
    def fromDict(dicionario_cliente) -> Cliente:
        email = _validarEmail(dicionario_cliente['email'])
        if 'uuid' in dicionario_cliente:
            uuid = dicionario_cliente['uuid']
        else:
            uuid = None
        return Cliente(nome=dicionario_cliente['nome'], email=email, uuid=None)
        