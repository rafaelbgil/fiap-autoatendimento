from src.gateways.PedidoRepositoryInterface import PedidoRepositoryInterface
from src.entities.Pedido import Pedido
from src.entities.PedidoFactory import PedidoFactory
from src.entities.ItemPedidoFactory import ItemPedidoFactory
from src.entities.TypeCpf import Cpf
from api.models import Pedido as PedidoModel
from api.models import ItemPedido as ItemPedidoModel
from api.models import Produto as ProdutoModel


class PedidoRepositoryOrm(PedidoRepositoryInterface):
    def listPedido() -> [Pedido]:
        pedidos_queryset = PedidoModel.objects.all()
        lista_pedidos = []

        if not pedidos_queryset:
            return lista_pedidos

        for pedido_orm in pedidos_queryset:
            lista_itens_orm = pedido_orm.itempedido_set.all()
            lista_itens = []
            for item in lista_itens_orm:
                lista_itens.append(item.__dict__)
            
            pedido_dict = pedido_orm.__dict__
            pedido_dict['numero'] = pedido_orm.id
            pedido_dict['lista_itens'] = lista_itens
            #pedido_dict['cpf'] =  pedido_orm.cpf          
            #pedido_dict['status'] = pedido_orm.status

            pedido = PedidoFactory.fromDict(
                dicionario_pedido=pedido_dict)
            lista_pedidos.append(pedido)
        
        return lista_pedidos

    def addPedidoFromDict(dicionario_pedido: dict):
        if not 'lista_itens' in dicionario_pedido:
            raise Exception('A lista de itens não pode ser vazia.')

        lista_itens = []
        valor_total = 0
        cpf = None
        # Verifica se produto consultado pelo id existe, cria um objeto ItemPedido e o adiciona a lista_itens
        for item in dicionario_pedido['lista_itens']:
            try:
                produto_model = ProdutoModel.objects.get(id=item['id'])
            except:
                raise Exception(
                    'Nao foi possivel localizar o item com id %s.' % (item['id']))
            item_pedido = ItemPedidoFactory.fromDict(dicionario_item=produto_model.__dict__)
            item_pedido.quantidade = item['quantidade']
            valor_total = valor_total + (item['quantidade'] * item_pedido.preco)
            lista_itens.append(item_pedido)

        if 'cpf' in dicionario_pedido:
            cpf = Cpf(cpf=dicionario_pedido['cpf'])
        
        pedido_orm = PedidoModel()
        pedido_orm.cpf = cpf
        pedido_orm.valor = valor_total
        try:
            pedido_orm.save()
        except:
            raise(Exception)
        
        for item_da_lista in lista_itens:
            item_pedido_orm = ItemPedidoModel()
            item_pedido_orm.pedido = pedido_orm
            item_pedido_orm.nome = item_da_lista.nome
            item_pedido_orm.descricacao = item_da_lista.descricao
            item_pedido_orm.quantidade = item_da_lista.quantidade
            item_pedido_orm.imagem_url = item_da_lista.imagem_url
            item_pedido_orm.preco = item_da_lista.preco
            try:
                item_pedido_orm.save()
            except:
                raise(Exception)
            
        return pedido_orm
