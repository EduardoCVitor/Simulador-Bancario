# PROJETO - CRIANDO UM SIMULADOR BANCÁRIO

# IMPORTS

import main_library as mainLib                                # Importa biblioteca com as funções do projeto
from datetime import date                                    # Importa biblioteca para manipulação de data

# DEFINIÇÃO DE FUNÇÃO

# Função para chamada do menu de opções por recursão
def menu_pessoa_fisica():
    print("")
    print("O que deseja fazer?")
    mainLib.exibir_menu(menu2)                               # Chama função que exibe o menu de opções
    op2 = int(input("Escolha uma opção: "))
    print("")

    if op2 == 0:                                             # Acessa a exibição das contas

        mainLib.listar_contasPF(listaContasPF, True)         # Chama função que lista todas as contas

    elif op2 == 1:                                           # Acessa o cadastro de contas

        nconta = input("Informe o número da conta: ")
        nome = input("Informe o nome do cliente: ")
        cpf = input("Informe o CPF do cliente: ")
        renda = float(input("Informe a renda do cliente: "))
        tempo = str(date.today().strftime('%d-%m-%Y'))       # Chama método que retorna data e a formata
        saldo = float(input("Informe o saldo da conta: "))

        # Instancia um objeto da classe Pessoa Física
        pessoa = mainLib.PessoaFisica(nconta, nome, saldo, tempo, cpf, renda)
        listaContasPF.append(pessoa)                         # Adiciona na lista de contas PF a nova conta.
        print(f"A conta de {nome} foi criada com sucesso")

    elif op2 == 2:                                           # Acessa a opção para remover contas

        mainLib.listar_contasPF(listaContasPF, True)         # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta a ser removida: ")
        # Imprime a mensagem específica substituindo a chamada da função pelo seu retorno
        print(f"Os dados da conta removida são {mainLib.remover_conta(nconta, listaContasPF)}")

    elif op2 == 3:                                           # Acessa a opção para alterar conta

        mainLib.listar_contasPF(listaContasPF, True)         # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta a ser alterada: ")
        conta = mainLib.buscar_conta(nconta, listaContasPF)  # Função que retorna conta baseada nos parametros
        nome = input("Informe o novo nome do Cliente: ")
        renda = float(input("Informe a nova renda do Cliente: "))
        conta.alterar_conta(nome, renda)                     # Função que altera conta baseada nos parametros passados
        print("")
        mainLib.exibe_data_hora()  # Chama função para exibir data e hora
        print("A conta foi alterada com sucesso")

    elif op2 == 4:                                           # Acessa a opção para fazer saque

        mainLib.listar_contasPF(listaContasPF, False)        # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta para saque: ")
        valor = float(input("Digite o valor do saque: "))
        conta = mainLib.buscar_conta(nconta, listaContasPF)  # Função que retorna conta baseada nos parametros
        print("")
        mainLib.exibe_data_hora()                            # Chama função para exibir data e hora
        conta.fazer_saque(valor)                             # Chama função sacar, passando o valor como parametro

    elif op2 == 5:  # Acessa a opção para fazer depósito

        mainLib.listar_contasPF(listaContasPF, False)        # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta para depósito: ")
        valor = float(input("Digite o valor do depósito: "))
        conta = mainLib.buscar_conta(nconta, listaContasPF)  # Função que retorna conta baseada nos parametros
        print("")
        mainLib.exibe_data_hora()                            # Chama função para exibir data e hora
        conta.fazer_deposito(valor)                          # Chama função depositar, passando o parametro valor

    elif op2 == 6:                                           # Acessa a opção para calcular o imposto

        mainLib.listar_contasPF(listaContasPF, False)        # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta para calcular o IRRF: ")
        conta = mainLib.buscar_conta(nconta, listaContasPF)  # Função que retorna conta baseada nos parametros
        print("")
        mainLib.exibe_data_hora()                            # Chama função para exibir data e hora
        conta.calcula_imposto()                              # Chama função para calcular o imposto

    elif op2 == 7:                                           # Acessa a opção para retornar ao menu principal

        print("Retornando para a seleção de sistemas")
        return                                               # Interrompe a recursão e volta ao menu principal

    else:                                                    # Executa caso nenhuma opção válida tenha sido escolhida
        print("")
        print("Opção inválida, escolha outra opção")

    menu_pessoa_fisica()                                     # Faz a chamada recursiva da função que exibe o menu


# Função para chamada do menu de opções por recursão
def menu_pessoa_juridica():
    print("")
    print("O que deseja fazer?")
    mainLib.exibir_menu(menu2)                               # Chama função que exibe o menu de opções
    op2 = int(input("Escolha uma opção: "))
    print("")

    if op2 == 0:                                             # Acessa o cadastro de contas

        mainLib.listar_contasPJ(listaContasPJ, True)         # Chama função que lista todas as contas

    elif op2 == 1:                                           # Acessa o cadastro de contas

        nconta = input("Informe o número da conta: ")
        razao_social = input("Informe a Razão Social da empresa: ")
        cnpj = input("Informe o CNPJ da empresa: ")
        tempo = str(date.today().strftime('%d-%m-%Y'))       # Chama método que retorna data e a formata
        print("O porte da empresa pode ser: pequeno, medio ou grande")
        porte = input("Informe o porte da empresa: ")
        faturamento = float(input("Informe o faturamento da empresa: "))
        saldo = float(input("Informe o saldo da conta: "))
        # Instancia um objeto da classe Pessoa Jurídica
        pessoa = mainLib.PessoaJuridica(nconta, saldo, tempo, razao_social, cnpj, porte, faturamento)
        listaContasPJ.append(pessoa)                         # Adiciona na lista de contas PJ a nova conta.
        print(f"A conta da {razao_social} foi criada com sucesso")

    elif op2 == 2:                                           # Acessa a opção para remover contas

        mainLib.listar_contasPJ(listaContasPJ, True)         # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta a ser removida: ")
        # Imprime a mensagem específica substituindo a chamada da função pelo seu retorno
        print(f"Os dados da conta removida são {mainLib.remover_conta(nconta, listaContasPJ)}")

    elif op2 == 3:                                           # Acessa a opção para alterar conta

        mainLib.listar_contasPJ(listaContasPJ, True)         # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta a ser alterada: ")
        conta = mainLib.buscar_conta(nconta, listaContasPJ)  # Função que retorna conta baseada nos parametros
        razao_social = input("Informe a nova Razão Social da empresa: ")
        print("O porte da empresa pode ser: pequeno, medio ou grande")
        porte = input("Informe o novo porte da empresa: ")
        faturamento = float(input("Informe o novo faturamento da empresa: "))
        conta.alterar_conta(razao_social, porte, faturamento)  # Função que altera conta baseada nos parametros
        print("")
        mainLib.exibe_data_hora()                            # Chama função para exibir data e hora
        print("A conta foi alterada com sucesso")

    elif op2 == 4:                                           # Acessa a opção para fazer saque

        mainLib.listar_contasPJ(listaContasPJ, False)        # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta para saque: ")
        valor = float(input("Digite o valor do saque: "))
        conta = mainLib.buscar_conta(nconta, listaContasPJ)  # Função que retorna conta baseada nos parametros
        print("")
        mainLib.exibe_data_hora()                            # Chama função para exibir data e hora
        conta.fazer_saque(valor)                             # Chama função sacar, passando o valor como parametro

    elif op2 == 5:                                           # Acessa a opção para fazer depósito

        mainLib.listar_contasPJ(listaContasPJ, False)        # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta para depósito: ")
        valor = float(input("Digite o valor do depósito: "))
        conta = mainLib.buscar_conta(nconta, listaContasPJ)  # Função que retorna conta baseada nos parametros
        print("")
        mainLib.exibe_data_hora()                            # Chama função para exibir data e hora
        conta.fazer_deposito(valor)                          # Chama função depositar, passando o parametro valor

    elif op2 == 6:                                           # Acessa a opção para calcular o imposto

        mainLib.listar_contasPJ(listaContasPJ, False)        # Chama função que lista todas as contas
        print("")
        nconta = input("Informe o número da conta para calcular o IRRF: ")
        conta = mainLib.buscar_conta(nconta, listaContasPJ)  # Função que retorna conta baseada nos parametros
        print("")
        mainLib.exibe_data_hora()                            # Chama função para exibir data e hora
        conta.calcula_imposto()                              # Chama função para calcular o imposto

    elif op2 == 7:                                           # Acessa a opção para retornar ao menu principal

        print("Retornando para a seleção de sistemas")
        return                                               # Interrompe a recursão e volta ao menu principal

    else:                                                    # Executa caso nenhuma opção válida tenha sido escolhida
        print("")
        print("Opção inválida, escolha outra opção")

    menu_pessoa_juridica()                                   # Faz a chamada recursiva da função que exibe o menu


# DECLARANDO VARIÁVEIS

# Definição das opções que comporão os menus do sistema
menu1 = ["Sistema para Pessoa Física", "Sistema para Pessoa Jurídica", "Sair do programa"]
menu2 = ["Listar Contas", "Cadastrar Conta", "Remover Conta", "Alterar Conta", "Fazer Saque",
         "Fazer Depósito", "Calcular Imposto", "Escolher outro sistema"]

# Inicializando as listas
listaContasPF = []
listaContasPJ = []

print("")
print("Bem vindo ao Banco Virtual 3.0")

while True:                                                 # Inicia a estrutura de repetição do sistema

    print("")
    print("Qual sistema deseja acessar?")
    mainLib.exibir_menu(menu1)                              # Chama função que exibe o menu de opções

    op1 = int(input("Escolha uma opção: "))

    if op1 == 0:                                            # Acessa o Sistema de Pessoa Física

        print("")
        print(f"Bem vindo ao {menu1[op1]}")
        menu_pessoa_fisica()                                # Chama função que exibe o menu de opções para PF

    elif op1 == 1:                                          # Acessa o Sistema de Pessoa Jurídica

        print("")
        print(f"Bem vindo ao {menu1[op1]}")
        menu_pessoa_juridica()                              # Chama função que exibe o menu de opções para PJ

    elif op1 == 2:
        print("")
        print("Finalizando...")
        break                                               # Finaliza a execução do programa

    else:
        print("")
        print("Opção inválida, escolha outra opção")
