from src.entities.Pedido import Pedido
class PedidoDto:
    def fromPedidoToDict(pedido: Pedido) -> dict:
        if not type(pedido) == Pedido:
            raise Exception('O objeto nao e do tipo Pedido')
        
        pedido_dict = pedido.__dict__
        pedido_dict['id'] = pedido_dict['numero']
        del(pedido_dict['numero'])
        if type(pedido.lista_itens) == list and len(pedido.lista_itens) > 0:
            lista_itens = []
            for item_pedido in pedido.lista_itens:
                item_pedido_dict = item_pedido.__dict__
                del(item_pedido_dict['id_categoria'])
                lista_itens.append(item_pedido_dict)
                
            del(pedido_dict['lista_itens'])  
            pedido_dict['lista_itens'] = lista_itens
            
        return pedido_dict

    def fromListPedidoToDict(lista_pedidos: [Pedido])-> [dict]:
        if not type(lista_pedidos) == list:
            raise Exception('O objeto nao e do tipo Lista Pedido')
        lista_pedidos_dict = []
        for pedido in lista_pedidos:
            lista_pedidos_dict.append(PedidoDto.fromPedidoToDict(pedido))
        
        return lista_pedidos_dict

