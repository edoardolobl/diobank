from abc import ABC, abstractmethod
from datetime import datetime
import textwrap


class Cliente:
    """Represents a bank customer."""

    def __init__(self, endereco: str):
        """Initializes a Cliente object.

        Args:
            endereco (str): The customer's address.
        """
        self._endereco = endereco
        self._contas: list['Conta'] = []

    @property
    def endereco(self) -> str:
        return self._endereco

    def adicionar_conta(self, conta: 'Conta'):
        """Adds an account to the customer's list of accounts."""
        self._contas.append(conta)

    def realizar_transacao(self, conta: 'Conta', transacao: 'Transacao'):
        """Performs a transaction on a specific account."""
        # We'll implement the transaction logic later
        pass


class PessoaFisica(Cliente):
    """Represents an individual customer (Pessoa Física)."""

    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        """Initializes a PessoaFisica object.

        Args:
            nome (str): The customer's full name.
            data_nascimento (str): The customer's date of birth in the format 'dd-mm-yyyy'.
            cpf (str): The customer's CPF (Brazilian tax ID).
            endereco (str): The customer's address.
        """
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento

    @property
    def cpf(self) -> str:
        return self._cpf


class Conta(ABC):
    """An abstract base class representing a bank account."""

    def __init__(self, numero: int, cliente: Cliente):
        """Initializes a Conta object.

        Args:
            numero (int): The account number.
            cliente (Cliente): The account holder (customer).
        """
        self._saldo: float = 0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: Cliente = cliente

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        """Withdraws money from the account.

        Args:
            valor (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        pass

    @abstractmethod
    def depositar(self, valor: float) -> bool:
        """Deposits money into the account.

        Args:
            valor (float): The amount to deposit.

        Returns:
            bool: True if the deposit was successful, False otherwise.
        """
        pass


class ContaCorrente(Conta):
    """Represents a checking account."""

    def __init__(self, numero: int, cliente: Cliente, limite: float = 500.0, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self._limite: float = limite
        self._limite_saques: int = limite_saques
        self._historico: Historico = Historico()  # Add history to the account

    def sacar(self, valor: float) -> bool:
        """Withdraws money from the checking account, taking into account limits."""

        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        if self._historico.contar_saques() >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        if valor > self._saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        self._saldo -= valor
        self._historico.adicionar_transacao(Saque(valor))  # Register the withdrawal transaction
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor: float) -> bool:
        """Deposits money into the checking account."""

        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        self._saldo += valor
        self._historico.adicionar_transacao(Deposito(valor))  # Register the deposit transaction
        print("\n=== Depósito realizado com sucesso! ===")
        return True

    # Add Historico and Transacao classes


class Historico:
    """Stores the transaction history of an account."""

    def __init__(self):
        self._transacoes: list['Transacao'] = []

    @property
    def transacoes(self) -> list['Transacao']:
        return self._transacoes

    def adicionar_transacao(self, transacao: 'Transacao'):
        """Adds a transaction to the history."""
        self._transacoes.append(transacao)

    def contar_saques(self) -> int:
        """Counts the number of withdrawals in the history."""
        return sum(1 for transacao in self._transacoes if isinstance(transacao, Saque))


class Transacao(ABC):
    """Abstract base class for bank transactions."""

    def __init__(self, valor: float):
        """Initializes a Transacao object.

        Args:
            valor (float): The amount of the transaction.
        """
        self._valor = valor
        self._data = datetime.now()

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def data(self) -> datetime:
        return self._data


class Saque(Transacao):
    """Represents a withdrawal transaction."""
    pass


class Deposito(Transacao):
    """Represents a deposit transaction."""
    pass


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def criar_cliente(clientes: list[PessoaFisica]):
    """Creates a new PessoaFisica (individual customer)."""

    cpf = input("Informe o CPF (somente número): ")
    if any(cliente.cpf == cpf for cliente in clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta: int, clientes: list[PessoaFisica], contas: list[ContaCorrente]):
    """Creates a new ContaCorrente (checking account)."""

    cpf = input("Informe o CPF do cliente: ")
    cliente = next((cliente for cliente in clientes if cliente.cpf == cpf), None)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente(numero=numero_conta, cliente=cliente)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("\n=== Conta criada com sucesso! ===")


def depositar(contas: list[ContaCorrente]):
    """Handles deposit operations."""
    numero_conta = int(input("Informe o número da conta: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if not conta:
        print("\n@@@ Conta não encontrada! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    conta.depositar(valor)


def sacar(contas: list[ContaCorrente]):
    """Handles withdrawal operations."""
    numero_conta = int(input("Informe o número da conta: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if not conta:
        print("\n@@@ Conta não encontrada! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    conta.sacar(valor)


def exibir_extrato(contas: list[ContaCorrente]):
    """Displays the account statement."""
    numero_conta = int(input("Informe o número da conta: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if not conta:
        print("\n@@@ Conta não encontrada! @@@")
        return

    print("\n================ EXTRATO ================")
    print(f"Cliente: {conta.cliente.nome}")  # Access customer's name
    print(f"Agência: {conta.agencia}")
    print(f"C/C: {conta.numero}")
    print(f"Saldo: R$ {conta.saldo:.2f}")

    if conta._historico.transacoes:
        for transacao in conta._historico.transacoes:
            print(f"- {transacao.__class__.__name__}: R$ {transacao.valor:.2f} ({transacao.data.strftime('%d-%m-%Y %H:%M:%S')})")
    else:
        print("Não foram realizadas movimentações.")
    print("==========================================")


def listar_contas(contas: list[ContaCorrente]):
    """Lists all accounts."""
    if not contas:
        print("\n@@@ Não existem contas cadastradas. @@@")
        return

    for conta in contas:
        print("=" * 100)
        print(f"Agência:\t{conta.agencia}")
        print(f"C/C:\t\t{conta.numero}")
        print(f"Titular:\t{conta.cliente.nome}")
        print("=" * 100)


def main():
    clientes: list[PessoaFisica] = []
    contas: list[ContaCorrente] = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(contas)

        elif opcao == "s":
            sacar(contas)

        elif opcao == "e":
            exibir_extrato(contas)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            criar_conta(numero_conta, clientes, contas)
            numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()

