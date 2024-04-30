import datetime

class ContaBancaria:
    """Representa uma conta bancária com operações básicas como depósito, saque e extrato."""

    def __init__(self):
        """Inicializa a conta bancária com saldo zero e sem transações."""
        self.saldo = 0.0
        self.historico_transacoes = []
        self.contador_saques = 0  # Contador para limitar o número de saques diários

    def depositar(self, valor):
        """Permite ao usuário depositar dinheiro na conta, se o valor for positivo."""
        if valor > 0:
            self.saldo += valor
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.historico_transacoes.append((timestamp, f"Depósito: R$ {valor:.2f}"))
            print("Depósito realizado com sucesso!")
        else:
            print("Valor de depósito deve ser positivo!")

    def sacar(self, valor):
        """Permite ao usuário sacar dinheiro da conta, respeitando o limite diário e de valor por saque."""
        if self.contador_saques < 3 and valor <= 500:
            if self.saldo >= valor:
                self.saldo -= valor
                self.contador_saques += 1
                timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                self.historico_transacoes.append((timestamp, f"Saque: R$ {valor:.2f}"))
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente para saque!")
        else:
            if self.contador_saques >= 3:
                print("Limite diário de saques atingido!")
            else:
                print("Valor de saque excede o limite de R$ 500.00!")

    def extrato(self):
        """Exibe o extrato da conta, mostrando todas as transações realizadas e o saldo atual."""
        print("\nExtrato das Transações:")
        print("-" * 40)
        for timestamp, transacao in self.historico_transacoes:
            print(f"{timestamp} - {transacao}")
        print("-" * 40)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")


def interface_usuario():
    """Fornece uma interface de usuário interativa para operar a conta bancária."""
    conta = ContaBancaria()
    while True:
        print("\n--- DIO BANK ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
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
                conta.sacar(valor)
            except ValueError:
                print("Por favor, insira um valor numérico.")
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
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
