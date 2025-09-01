nome = "Daniel"

mensagem = f"""
    Olá meu nome é {nome},
Eu estou aprendendo Python.
      essa mensagem tem diferentes recuos.
"""

print(mensagem)


print("""
      
      ============ MENU ============
      
      1 - Depositar
      2 - Sacar
      0 - Sair
      
      ==============================
      
            Obrigado por usar nosso sistema!!!
""")



# Sistema Bancário Simples

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def saque(valor, saldo, extrato, numero_saques):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite_saque:
        print("Operação falhou! Valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=============================\n")

# Menu Principal
while True:
    print("""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """)
    
    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(valor, saldo, extrato, numero_saques)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato)

    elif opcao == "q":
        print("Saindo do sistema... Obrigado por utilizar nosso banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente.")






# Sistema Bancário Simples sem funções e com histórico de operações

saldo = 0
limite_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3
movimentacoes = []  # Lista para armazenar depósitos e saques

while True:
    print("""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """)
    
    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            movimentacoes.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite_saque:
            print("Operação falhou! Valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            movimentacoes.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        if len(movimentacoes) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for mov in movimentacoes:
                print(mov)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================\n")

    elif opcao == "q":
        print("Saindo do sistema... Obrigado por utilizar nosso banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente.")