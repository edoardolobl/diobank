# DIOBankSystem

## Descrição

O **DIOBankSystem** é um projeto desenvolvido como parte do desafio "Criando um Sistema Bancário com Python" do Bootcamp "Python AI Backend Developer VIVO" na plataforma Digital Innovation One (DIO). Este sistema permite realizar operações bancárias básicas como depósito, saque e consulta de extratos através de uma interface de linha de comando.

## Funcionalidades

- **Depositar:** Permite ao usuário adicionar fundos à sua conta.
- **Sacar:** Permite ao usuário retirar fundos da conta, respeitando o limite de três saques diários e o máximo de R$ 500 por saque.
- **Extrato:** Mostra um extrato detalhado de todas as transações realizadas, incluindo depósitos e saques, com a data e o horário de cada operação.
- **Criar Usuário:** Permite ao sistema registrar um novo usuário com informações como nome, data de nascimento, CPF e endereço.
- **Criar Conta Corrente:** Permite criar uma conta corrente vinculada a um usuário existente, com número de conta sequencial.
- **Listar ou Buscar Contas:** Permite visualizar todas as contas cadastradas ou buscar contas específicas por nome do cliente ou CPF.

## Tecnologias Utilizadas

- **Python 3.8** ou superior

## Como Executar

Para executar o **DIOBankSystem**, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/DIOBankSystem.git

2. **Navegue até o diretório do projeto:**
   ```bash
   cd DIOBankSystem

4. **Execute o programa:**
   ```bash
   python diobank.py  
