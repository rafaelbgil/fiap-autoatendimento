from .Cliente import Cliente
import re


def _validarEmail(email: str) -> str:
    if email == None:
        raise Exception('E-mail não preenchido.')

    if not re.search('@', email):
        raise Exception('E-mail inválido.')

    if not re.search('\.', email):
        raise Exception('E-mail inválido.')

    if not re.match('^[a-z0-9][\w.-]*@[a-z0-9][\w.-]*[a-z0-9]$', email):
        raise Exception('E-mail inválido.')
    return email


def _validarUuid(uuid: str) -> str:
    if not uuid:
        return None

    uuid_formatado = uuid.replace('-', '').lower()

    if re.match('[^a-z0-9]', uuid_formatado):
        raise Exception('O UUID informado é inválido')
    
    if len(uuid_formatado) != 32:
        raise Exception('O UUID informado é inválido')
    return uuid_formatado


class ClienteFactory:
    def fromDict(dicionario_cliente: dict) -> Cliente:
        if 'email' in dicionario_cliente:
            email = _validarEmail(dicionario_cliente['email'])
        else:
            email = None

        if 'uuid' in dicionario_cliente:
            uuid = _validarUuid(dicionario_cliente['uuid'])
        else:
            uuid = None

        if 'nome' in dicionario_cliente:
            nome = dicionario_cliente['nome']
        else:
            nome = None

        return Cliente(nome=nome, email=email, uuid=uuid)
