menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))

        if valor <= 0:
            print("Valor inválido: depósito só suporta quantias positivas.")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == "s":
        valor = float(input("Valor do saque: "))

        if numero_saques >= LIMITE_SAQUES:
            print("Operação excederia limite de saques diários.")
        elif valor <= 0:
            print("Valor inválido: saque só suporta quantias positivas.")
        elif valor > LIMITE:
            print("Operação excederia limite por saque.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        if extrato:
            print(extrato)
        else:
            print("Extrato vazio.")
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
