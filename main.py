import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

balance = 0
limit = 500
statement = ""
withdrawals_number = 0
WITHDRAWS_LIMIT = 3
transactions_number = 0
TRANSACTIONS_LIMIT = 10

while True:

    option = input(menu)

    if transactions_number >= TRANSACTIONS_LIMIT and option != "e" and option != "q":
        print("Limite de transações diárias atingido.")
        continue

    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if option == "d":
        value = float(input("Informe o valor do depósito: "))
        balance += value
        statement += f"{date} => Depósito: R$ {value:.2f}\n"
        transactions_number += 1

    elif option == "s":
        if withdrawals_number >= WITHDRAWS_LIMIT:
            print("Limite de saques diários atingido.")
            continue

        value = float(input("Informe o valor do saque: "))

        if value > limit:
            print("Limite de saque excedido.")
            continue

        if balance >= value:
            balance -= value
            statement += f"{date} => Saque: R$ {value:.2f}\n"
            withdrawals_number += 1
            transactions_number += 1
        else:
            print("Saldo insuficiente")

    elif option == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações" if not statement else statement)
        print(f"\ndSaldo: R$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")