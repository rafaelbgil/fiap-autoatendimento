# Repositório Autoatendimento Lanchonete - Fiap Pós-Tech Arquitetura de Software

## Objetivo
O objetivo desse repositório é a apresentação da solução de autoatendimento proposta para o curso de pós gradução em **Arquitetura de Software**, aqui serão encontrados:
- Links de documentações ou entregáveis
- Código fonte da aplicação
- Código fonte de infraestrutura como código(caso necessário)
- Código fonte de Dockerfiles ou arquivos relacionados.

## DDD
A documentaração referente a parte do DDD(Domain Driven Design).
Link de acesso: [Documentação via miro](https://miro.com/app/board/uXjVMnTeAN8=/?share_link_id=984815149799)

No miro há os seguintes elementos:
- Glossário de linguagem ubíqua com os termos utilizados no dominio
- Pictograma com os fluxos
- Storytelling escrito
- Event Storming com os eventos
- Event Storming com a definição dos agredados

## Execução do composer

``` $ git clone https://github.com/rafaelbgil/fiap-autoatendimento.git ```


``` $ cd fiap-autoatendimento ```


``` $ docker-compose up ```


## URLS úteis:
swagger : http://127.0.0.1:8000/api/swagger

redoc: http://127.0.0.1:8000/api/redoc

## URLS das apis:
http://127.0.0.1:8000/api/cliente 

http://127.0.0.1:8000/api/categoria

http://127.0.0.1:8000/api/produto

http://127.0.0.1:8000/api/pedido