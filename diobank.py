import datetime

# Armazenamento de dados
usuarios = []  # Lista para armazenar os usuários
contas = []  # Lista para armazenar as contas

class ContaBancaria:
    """Representa uma conta bancária com operações básicas como depósito, saque e extrato."""

    def __init__(self):
        """Inicializa a conta bancária com saldo zero e sem transações."""
        self.saldo = 0.0
        self.historico_transacoes = []
        self.contador_saques = 0  # Contador para limitar o número de saques diários

    def depositar(self, valor, /):
        """Permite ao usuário depositar dinheiro na conta. Argumento valor deve ser positivo e é posicional-only."""
        if valor > 0:
            self.saldo += valor
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.historico_transacoes.append((timestamp, f"Depósito: R$ {valor:.2f}"))
            print("Depósito realizado com sucesso!")
        else:
            print("Valor de depósito deve ser positivo!")

    def sacar(self, *, saldo, valor, extrato, limite=500, numero_saques, limite_saques=3):
        """Permite ao usuário sacar dinheiro da conta com argumentos keyword-only."""
        if numero_saques < limite_saques and valor <= limite:
            if saldo >= valor:
                saldo -= valor
                numero_saques += 1
                timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                extrato.append((timestamp, f"Saque: R$ {valor:.2f}"))
                print("Saque realizado com sucesso!")
                return saldo, extrato
            else:
                print("Saldo insuficiente para saque!")
        else:
            if numero_saques >= limite_saques:
                print("Limite diário de saques atingido!")
            else:
                print("Valor de saque excede o limite de R$ 500.00!")

    def extrato(self, saldo, /, *, extrato):
        """Exibe o extrato da conta, mostrando todas as transações realizadas e o saldo atual. Argumentos posicionais e nomeados."""
        print("\nExtrato das Transações:")
        print("-" * 40)
        for timestamp, transacao in extrato:
            print(f"{timestamp} - {transacao}")
        print("-" * 40)
        print(f"Saldo atual: R$ {saldo:.2f}\n")


def criar_usuario(nome, data_nascimento, cpf, endereco):
    """Cria um novo usuário se o CPF não estiver duplicado."""
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere não numérico do CPF
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro: Já existe um usuário com este CPF.")
    else:
        usuario = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
        usuarios.append(usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")


def criar_conta_corrente(cpf):
    """Cria uma conta corrente para um usuário existente com um número de conta sequencial."""
    cpf = ''.join(filter(str.isdigit, cpf))  # Garante que o CPF esteja no formato correto
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if usuario is not None:
        numero_conta = len(contas) + 1  # Número sequencial da conta
        conta = {'agencia': '0001', 'numero_conta': numero_conta, 'usuario': usuario}
        contas.append(conta)
        print(f"Conta corrente {numero_conta} criada para o usuário {usuario['nome']} na agência 0001.")
    else:
        print("Erro: Usuário não encontrado. Por favor, cadastre o usuário primeiro.")


def listar_ou_buscar_contas(nome_cliente=None, cpf_cliente=None):
    """Lista todas as contas ou busca contas específicas pelo nome do cliente ou CPF."""
    cpf_cliente = ''.join(filter(str.isdigit, cpf_cliente)) if cpf_cliente else None
    contas_filtradas = [
        conta for conta in contas
        if (nome_cliente in conta['usuario']['nome'] if nome_cliente else True) and
           (cpf_cliente == conta['usuario']['cpf'] if cpf_cliente else True)
    ]

    if contas_filtradas:
        print("\n--- Contas Cadastradas ---")
        print(f"{'Agência':<10}{'Número da Conta':<20}{'Nome do Titular':<25}{'CPF':<15}")
        print("-" * 70)
        for conta in contas_filtradas:
            usuario = conta['usuario']
            print(f"{conta['agencia']:<10}{conta['numero_conta']:<20}{usuario['nome']:<25}{usuario['cpf']:<15}")
        print("-" * 70)
    else:
        print("Não foram encontradas contas com os critérios especificados.")


def interface_usuario():
    """Fornece uma interface de usuário interativa para operar a conta bancária e gerenciar usuários e contas."""
    conta = ContaBancaria()
    while True:
        print("\n--- DIO BANK ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Criar Usuário")
        print("5. Criar Conta Corrente")
        print("6. Listar ou Buscar Contas")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Informe o valor a ser depositado: R$ "))
                conta.depositar(valor)
            except ValueError:
                print("Por favor, insira um valor numérico.")
        elif opcao == '2':
            try:
                valor = float(input("Informe o valor a ser sacado: R$ "))
                saldo_atual, extrato_atual = conta.sacar(saldo=conta.saldo, valor=valor, extrato=conta.historico_transacoes)
                conta.saldo, conta.historico_transacoes = saldo_atual, extrato_atual
            except ValueError:
                print("Por favor, insira um valor numérico.")
        elif opcao == '3':
            conta.extrato(conta.saldo, extrato=conta.historico_transacoes)
        elif opcao == '4':
            nome = input("Nome do usuário: ")
            data_nascimento = input("Data de nascimento (dd/mm/yyyy): ")
            cpf = input("CPF (apenas números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == '5':
            cpf = input("CPF do usuário para criar conta (apenas números): ")
            criar_conta_corrente(cpf)
        elif opcao == '6':
            print("\nOpções de Busca:")
            print("a. Listar todas as contas")
            print("b. Buscar conta por nome")
            print("c. Buscar conta por CPF")
            sub_opcao = input("Escolha uma opção de busca: ")
            if sub_opcao == 'a':
                listar_ou_buscar_contas()
            elif sub_opcao == 'b':
                nome_cliente = input("Digite o nome do cliente: ")
                listar_ou_buscar_contas(nome_cliente=nome_cliente)
            elif sub_opcao == 'c':
                cpf_cliente = input("Digite o CPF do cliente (apenas números): ")
                listar_ou_buscar_contas(cpf_cliente=cpf_cliente)
        elif opcao == '7':
            print("Obrigado por usar o DIO Bank!")
            break
        else:
            print("Opção inválida, tente novamente!")


def main():
    """Ponto de entrada principal do programa."""
    print("Bem-vindo ao Sistema Bancário DIO Bank!")
    interface_usuario()


if __name__ == "__main__":
    main()
