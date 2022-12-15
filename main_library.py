# IMPORTS

from datetime import datetime           # Importa biblioteca para manipulação de data e hora
import json                             # Importa biblioteca para manipulação de arquivos JSON

# DEFININDO CLASSES


# Definindo a Super Classe
class Pessoa:

    # Criando o contrutor da class Pessoa
    def __init__(self, conta, saldo, tempo):
        # Definindo atributos
        self.conta = conta
        self.saldo = saldo
        self.tempo = tempo

    # Método para fazer saques nas contas
    def fazer_saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque realizado, o saldo atual é R$ {self.saldo}")
        else:
            print(f"O saldo em conta é R$ {self.saldo}, insuficiente para um saque de R$ {valor}")

    # Método para fazer depósitos nas contas
    def fazer_deposito(self, valor):
        self.saldo += valor
        print(f"Depósito realizado, o saldo atual é R$ {self.saldo}")

    # Método para calcular imposto, este método é abstrato e deverá ser definido nas classes herdeiras.
    def calcula_imposto(self):
        pass


# Definindo Classe que herda da Super Classe
class PessoaFisica(Pessoa):
    # Criando o contrutor da class PessoaFisica
    def __init__(self, conta, cliente, saldo, tempo, cpf, renda):
        super().__init__(conta, saldo, tempo)
        # Definindo atributo
        self.cliente = cliente
        self.cpf = cpf
        self.renda = renda

    # Definindo como objeto da classe será impresso de modo a facilitar sua visualização
    def __str__(self):
        return (f"Conta: [{self.conta}], Cliente: {self.cliente}, CPF: {self.cpf}, Renda: {self.renda},"
                f" Cliente desde: {self.tempo}, Saldo: {self.saldo}")

    # Métodos para alterar os dados da conta
    def alterar_conta(self, cliente, renda):
        self.cliente = cliente
        self.renda = renda

    # Métodos para cálculo do imposto devido
    def calcula_imposto(self):
        print(f"{self.cliente}, para sua renda de R$ {self.renda}, o valor do imposto é R$ {self.renda * 0.09}")


# Definindo Classe que herda da Super Classe
class PessoaJuridica(Pessoa):
    # Criando o contrutor da class PessoaJuridica
    def __init__(self, conta, saldo, tempo, razao_social, cnpj, porte, faturamento):
        super().__init__(conta, saldo, tempo)
        # Definindo atributos
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.porte = porte
        self.faturamento = faturamento

    # Definindo como objeto da classe será impresso de modo a facilitar sua visualização
    def __str__(self):
        return (f"Conta: [{self.conta}], Razao Social: {self.razao_social}, CNPJ: {self.cnpj},"
                f" Faturamento: {self.faturamento}, Porte: {self.porte},"
                f" Cliente desde: {self.tempo}, Saldo: {self.saldo}")

    # Métodos para alterar os dados da conta
    def alterar_conta(self, razao_social, porte, faturamento):
        self.razao_social = razao_social
        self.porte = porte
        self.faturamento = faturamento

    # Métodos para cálculo do imposto devido
    def calcula_imposto(self):
        if self.porte == "pequeno":
            print(f"{self.razao_social} - porte {self.porte} - imposto devido de R$ {self.faturamento * 0.12}")
        elif self.porte == "medio":
            print(f"{self.razao_social} - porte {self.porte} - imposto devido de R$ {self.faturamento * 0.19}")
        elif self.porte == "grande":
            print(f"{self.razao_social} - porte {self.porte} - imposto devido de R$ {self.faturamento * 0.27}")


# DEFININDO FUNÇÕES

# Função que pega a data e hora e a imprime segundo formatação desejada
def exibe_data_hora():
    data_hora = datetime.now()
    print(data_hora.strftime("%d-%m-%Y %H:%M:%S"))


# Função que varre uma lista retornando os indices e valores da mesma
def exibir_menu(menu):
    for i, v in enumerate(menu):
        print(f"[{i}] {v}")


# Função que varre uma lista imprimindo os objetos da mesma
def listar_contasPF(lista, opcao):
    if opcao:
        if len(lista) != 0:
            for conta in lista:
                print(conta)
        else:
            print("Não existem contas cadastradas!")
    else:
        if len(lista) != 0:
            for conta in lista:
                print(f"Conta: [{conta.conta}], Cliente: {conta.cliente}, Saldo: {conta.saldo}")
        else:
            print("Não existem contas cadastradas!")


# Função que varre uma lista imprimindo os objetos da mesma
def listar_contasPJ(lista, opcao):
    if opcao:
        if len(lista) != 0:
            for conta in lista:
                print(conta)
        else:
            print("Não existem contas cadastradas!")
    else:
        if len(lista) != 0:
            for conta in lista:
                print(f"Conta: [{conta.conta}], Cliente: {conta.razao_social}, Saldo: {conta.saldo}")
        else:
            print("Não existem contas cadastradas!")


# Função para remover uma conta do sistema
def remover_conta(numero_conta, lista):
    for c, cont in enumerate(lista):
        if numero_conta == cont.conta:
            return lista.pop(c)


# Função que recebe o número de uma conta e retorna a conta correspondente
def buscar_conta(numero_conta, lista):
    for conta in lista:
        if numero_conta == conta.conta:
            return conta
        else:
            print("O número da conta não existe.")
