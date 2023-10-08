from .Categoria import Categoria

def _validar_nome_categoria(nome) -> str:
    if len(nome) > 40:
        raise Exception('Excedido o tamanho máximo de caracteres para categoria(max: 40).')
    if len(nome) == 0:
        raise Exception('Nome da categoria definido como vazio.')


class CategoriaFactory:
    def fromDict(dicionario_categoria) -> Categoria: 
        if 'nome' in dicionario_categoria:
            nome = _validar_nome_categoria(dicionario_categoria['nome'])
        else:
            raise Exception('Nome da categoria não preenchido.')
        
        return Categoria(nome=nome)