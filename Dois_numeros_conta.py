while True:
    first_value = float(input("Digite um número: "))
    operator = input("Escolha seu operador (+, -, * or /): ")
    second_value = float(input("Digite outro número: "))

    if operator == "+":
        account = first_value + second_value
        print(account)

    elif operator == "-":
        account = first_value - second_value
        print(account)

    elif operator == "*":
        account = first_value * second_value
        print(account)

    elif operator == "/":
        if second_value == 0:
            print("Impossível dividir usando 0")
        else:
            account = first_value / second_value
            print(account)
    else:
        print("Operador inválido!")

    answer = input("Tentar novamente? (Sim/Não): ")
    if answer.lower() == "nao" or answer.lower() == "não":
        break