from api.models import Cliente as ClienteModel
from src.domain.entities.Cliente import Cliente
from src.domain.entities.ClienteFactory import ClienteFactory
from src.ports.ClienteDaoInterface import ClienteDaoInterface



class ClienteDaoOrm(ClienteDaoInterface):
    def getCliente(self, uuid: str) -> Cliente:
        client_uuid_validado = ClienteFactory.fromDict({'uuid' : uuid}).uuid
        try:
            cliente = ClienteModel.objects.get(uuid=client_uuid_validado)
        except:
            return False
        return ClienteFactory.fromDict(dicionario_cliente=cliente.__dict__, validar_campos=False)

    def listCliente(self) -> list[Cliente]:
        clientes_queryset = ClienteModel.objects.all()
        clientes = []
        for cliente in clientes_queryset.iterator():
            clientes.append(ClienteFactory.fromDict(
                dicionario_cliente=cliente.__dict__, validar_campos=False))
        return clientes

    def deleteCliente(self, uuid: str) -> bool:
        try:
            ClienteModel.objects.get(uuid=uuid).delete()
        except:
            return False
        return True

    def addCliente(self, cliente: Cliente):
        cliente_orm = ClienteModel()
        for atributo in cliente.__dict__.keys():
            if cliente.__dict__[atributo] and cliente.__dict__[atributo] != 'None':
                cliente_orm.__setattr__(atributo, cliente.__dict__[atributo])
        
        try:
            cliente_orm.save()
        except Exception as erro:
            if 'cpf' in erro.__str__() and 'UNIQUE' in erro.__str__():
                raise Exception ('Não foi possível adicionar o cliente, o CPF já está em uso.')

            if 'email' in erro.__str__() and 'UNIQUE' in erro.__str__():
                raise Exception ('Não foi possível adicionar o cliente, o e-mail já está em uso.')
            raise Exception('Não foi possível cadastrar o cliente.')
        
        cliente.setUuid(cliente_orm.uuid)
        return cliente

