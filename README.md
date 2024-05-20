# DIOBankSystem

## Descrição

O **DIOBankSystem** é um projeto desenvolvido como parte do desafio "Criando um Sistema Bancário com Python" do Bootcamp "Python AI Backend Developer VIVO" na plataforma Digital Innovation One (DIO). Este sistema permite realizar operações bancárias básicas como depósito, saque e consulta de extratos através de uma interface de linha de comando.

<br>

> ## Registro de Alterações
>
> **Versão 2.0.0 (27/10/2023)**
>
> **Refatoração e Melhorias Significativas:**
>
> - **Design Orientado a Objetos:** O código foi completamente reestruturado para seguir os princípios da programação orientada a objetos. Isso inclui:
>    - Definir classes para `Cliente`, `PessoaFisica`, `Conta` (classe base abstrata), `ContaCorrente`, `Historico` (histórico de transações), `Transacao` > > (classe base abstrata), `Saque` e `Deposito`.
>   - Usar encapsulamento para proteger atributos e métodos dentro das classes, fornecendo acesso controlado por meio de propriedades e métodos.
>   - Utilizar herança para criar uma hierarquia clara de classes (por exemplo, `PessoaFisica` herdando de `Cliente`).
>    - Implementar classes base abstratas (`Conta` e `Transacao`) para definir interfaces comuns para tipos de conta e tipos de transação, respectivamente.
>
> - **Manipulação de Dados Aprimorada:**
>    - O uso de listas de dicionários para armazenar `usuarios` e `contas` foi substituído por listas de objetos, o que é mais eficiente e gerenciável em um > contexto orientado a objetos.
>    - O histórico de transações agora está diretamente associado aos objetos `ContaCorrente` usando a classe `Historico`, tornando-o mais organizado e fácil de acessar.
>
> - **Interface do Usuário Aprimorada:**
>    - A interface do usuário permanece baseada em console, mas foi aprimorada com prompts mais claros e formatação de saída mais organizada.
>    - A estrutura do menu é mais concisa e fácil de usar.
>
> - **Clareza e Manutenibilidade do Código:**
>    - Adição de dicas de tipo para melhorar a legibilidade do código e ajudar na verificação de erros.
>    - Inclusão de docstrings abrangentes para documentar o propósito e o uso de classes e métodos, aprimorando a capacidade de manutenção e colaboração.
>
> - **Melhorias na Funcionalidade:**
>    - O método de saque (`sacar`) em `ContaCorrente` agora impõe corretamente os limites de saque (valor e número de saques por dia).
>    - O extrato da conta (`exibir_extrato`) agora exibe as transações com carimbos de data/hora para melhor acompanhamento.
>
> **Correções de Bugs:**
>
> - Resolvidos problemas com validação e manipulação de CPF.
> - Corrigidos erros potenciais relacionados a tipos de dados durante a entrada do usuário.
>
> **Versão Anterior (1.0.0):**
>
> - A versão anterior do código era uma implementação básica e procedural de um sistema bancário. Faltava design orientado a objetos, tinha estruturas de dados menos organizadas e tinha limitações em funcionalidade e interface do usuário.
> - O registro de alterações acima destaca as melhorias significativas introduzidas na Versão 2.0.0 para aprimorar a estrutura, a funcionalidade e a capacidade de manutenção do código. 

<br>

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
