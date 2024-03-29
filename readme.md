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

## Execução no composer

``` $ git clone https://github.com/rafaelbgil/fiap-autoatendimento.git ```


``` $ cd fiap-autoatendimento ```


``` $ docker-compose up ```

## Execução no Kubernetes
``` $ git clone https://github.com/rafaelbgil/fiap-autoatendimento.git ```

``` $ cd fiap-autoatendimento ```

``` $ kubectl apply -f k8s ```



**Para executar migrations do banco e carga de dados execute:**

``` kubectl exec deploy/app-autoatendimento -c fiap-pos-tech -- /bin/sh /app/carregar_dados.sh ```

## Arquitetura da solução
![arquitetura](https://github.com/rafaelbgil/fiap-autoatendimento/assets/13522522/ec957ea0-8f1e-4acd-93bc-907e953f2a8b)

## URLS úteis:
swagger : http://127.0.0.1:30555/api/swagger

redoc: http://127.0.0.1:30555/api/redoc

## URLS das apis:
http://127.0.0.1:30555/api/cliente 

http://127.0.0.1:30555/api/categoria

http://127.0.0.1:30555/api/produto

http://127.0.0.1:30555/api/pedido
