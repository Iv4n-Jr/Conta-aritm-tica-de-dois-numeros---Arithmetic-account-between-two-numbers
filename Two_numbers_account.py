while True:
    first_value = float(input("Type one number: "))
    operator = input("Choose your operator (+, -, * or /): ")
    second_value = float(input("Type another number: "))

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
            print("Impossible to divide by 0")
        else:
            account = first_value / second_value
            print(account)
    else:
        print("Invalid operator!")

    answer = input("Try again? (Yes/No): ")
    if answer.lower() == "no":
        break