# Sistema Bancário v1.0

saldo = 0
limite_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""  # Armazena todas as movimentações em formato de texto

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
            extrato += f"Depósito: R$ {valor:.2f}\n"
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
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato, end="")  # mostra todas as movimentações já concatenadas
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================\n")

    elif opcao == "q":
        print("Saindo do sistema... Obrigado por utilizar nosso banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente.")


