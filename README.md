# Sistema Bancário POO em Python

## Descrição

Implementação de um sistema bancário simples, utilizando conceitos de Programação Orientada a Objetos (POO) em Python. 
O objetivo foi desenvolver uma aplicação divida em módulos, organizada no padrão MVC (Model-View-Controller), 
que simula algumas operações bancárias básicas, como criação de contas, depósitos, saques, visualização de extratos e verificação de saldo.

## Funcionalidades

- **Criação de Clientes**: Permite a criação de novos clientes com informações pessoais.
- **Criação de Contas**: Permite a abertura de novas contas bancárias para os clientes cadastrados, com agência fixa em "2408" e número de conta corrente começando em "0001" e sendo incrementado de 1 em 1 automaticamente.
- **Depósitos**: Permite realizar depósitos em contas existentes.
- **Saques**: Permite realizar saques de contas existentes, respeitando limites e saldo disponível.
- **Extrato**: Exibe o histórico de transações de uma conta.
- **Ver Saldo**: Exibe o saldo atual de uma conta.
- **Listagem de Contas**: Lista todas as contas existentes no sistema.
- **Listagem de Clientes**: Lista todos os clientes cadastrados no sistema.

## Estrutura do Projeto

O projeto segue o padrão MVC, que separa a lógica de negócio (Models), a lógica de controle (Controllers) e a interface do usuário (Views).


### Modelos (Models)

- **Cliente**: Representa um cliente bancário.
- **Conta**: Representa uma conta bancária geral.
- **ContaCorrente**: Especialização de Conta com limite de saques e valores.
- **Deposito**: Representa uma transação de depósito.
- **Historico**: Mantém o histórico de transações de uma conta.
- **PessoaFisica**: Especialização de Cliente com informações pessoais adicionais.
- **Saque**: Representa uma transação de saque.
- **Transacao**: Classe abstrata base para diferentes tipos de transações.

### Controladores (Controllers)

- **cliente_controller.py**: Lida com a lógica de negócio relacionada a clientes.
- **conta_controller.py**: Lida com a lógica de negócio relacionada a contas bancárias.

### Visões (Views)

- **menu_view.py**: Gerencia a interface de usuário através de um menu interativo no terminal.

### Como Executar

1. Clone o repositório:
   ```No seu Terminal digite o comando abaixo:
   git clone https://github.com/seu_usuario/sistema_bancario_poo.git
   OBS: seu_usuario deve ser trocado pelo nome do seu usuario no GitHub

### Contribuição
Sinta-se à vontade para contribuir com este projeto. Você pode abrir issues para relatar bugs ou sugerir melhorias, e enviar pull requests com novas funcionalidades ou correções de código.

### Contato
Se tiver alguma dúvida ou sugestão, entre em contato:

Email: needslucas944@gmail.com

LinkedIn: https://www.linkedin.com/in/lucas-ferreira-55053412a/

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.



