from src.domain.entities.Pedido import Pedido
from src.domain.entities.ItemPedido import ItemPedido
#from src.domain.entities.ProdutoFactory import ProdutoFactory
from src.domain.entities.TypeCpf import _validate_cpf

def _validar_lista_itens(lista_itens :  list) -> [ItemPedido]:
    if not type(lista_itens) == list:
        raise Exception('Lista de produtos deve ser uma lista/array')
    
    lista_itens_validados = []
    for produto in lista_itens:
        produto_validado = ProdutoFactory.fromDict(dicionario_produto=produto)
        lista_itens.append(lista_itens_validados)
    
    return lista_itens_validados
    
def _validar_valor(valor: float):
    if type(valor) != float and type(valor) != int:
        raise Exception('O valor deve ser numério, float ou int.')
    
    if valor <= 0:
        raise Exception('O valor deve ser maior que 0')

    return float(valor)

class PedidoFactory:
    @staticmethod
    def fromDict(dicionario_pedido: dict):
        numero = None
        cpf = None
        valor = 0
        if 'lista_itens' in dicionario_pedido:
            lista_itens = _validar_lista_itens(dicionario_pedido['lista_itens'])
        else:
            lista_itens = []

        if cpf in dicionario_pedido:
            cpf = _validate_cpf(dicionario_pedido['cpf'])
        
        for produto in lista_itens:
            valor = valor + produto
        
        valor = _validar_valor(valor=valor)

        return Pedido(numero=numero, lista_itens=lista_itens, valor=valor, cpf=cpf)


