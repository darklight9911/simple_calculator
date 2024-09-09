
while True:
    usr_input = input("Enter your calculation: ")
    try:
        if usr_input not in ["exit", "Exit"]:

            num1 = int(usr_input.split(" ")[0])
            operator = usr_input.split(" ")[1]
            num2 = int(usr_input.split(" ")[2])

            if operator.lower() in ["+", "add", "plus"]:
                print(num1 + num2)
            if operator.lower() in ["-", "sub", "minus"]:
                print(num1 - num2)
            if operator.lower() in ["*", "multiply", "into"]:
                print(num1 * num2)
            if operator.lower() in ["/", "divide", "by"]:
                print(num1 / num2)
        else:
            print("Exiting..")
            break
    except ValueError as err:
        print("Insert space separated input.")

