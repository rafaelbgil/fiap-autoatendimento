from .Cliente import Cliente
from .TypeCpf import Cpf
from uuid import UUID
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


def _validarUuid(uuid: str | UUID) -> str:
    if not uuid:
        return None

    if type(uuid) == UUID:
        uuid = uuid.__str__()

    uuid_formatado = uuid.replace('-', '').lower()

    if re.match('[^a-z0-9]', uuid_formatado):
        raise Exception('O UUID informado é inválido')
    
    if len(uuid_formatado) != 32:
        raise Exception('O UUID informado é inválido')
    return uuid_formatado

def _validarNome(nome: str) -> str:
    if nome and len(nome) > 1:
        return nome
    raise Exception('O nome deve ser informado')

class ClienteFactory:
    def fromDict(dicionario_cliente: dict, validar_campos=True) -> Cliente:
        nome = None
        email = None
        uuid = None
        cpf = None

        if 'email' in dicionario_cliente:
            if validar_campos:
                email = _validarEmail(dicionario_cliente['email'])
            else:
                email = dicionario_cliente['email']
       
        if 'uuid' in dicionario_cliente:
            if validar_campos:
                uuid = _validarUuid(dicionario_cliente['uuid'])
            else:
                uuid = dicionario_cliente['uuid'].__str__().replace('-','')

        if 'nome' in dicionario_cliente:
                if validar_campos:
                    nome = _validarNome(dicionario_cliente['nome'])
                else:
                    nome = dicionario_cliente['nome']

        if 'cpf' in dicionario_cliente:
            cpf = Cpf(cpf=dicionario_cliente['cpf']).cpf

        return Cliente(nome=nome, email=email, uuid=uuid, cpf=cpf)
