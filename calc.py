import sys
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
        add_list = ["+", "add", "plus"]
        minus_list = ["-", "sub", "minus"]
        multi_list = ["*", "multiply", "into"]
        div_list = ["/", "divide", "by"]
        all_list = add_list + minus_list + multi_list + div_list
        for i in all_list:

            try:
                # print(i)
                num1 = int(usr_input.split(i)[0])
                operator = i #comment
                num2 = int(usr_input.split(i)[1])
                # print(operator, num1, num2)
                if operator in add_list:
                    print(num1 + num2)
                elif operator in minus_list:
                    print(num1 - num2)
                elif operator in multi_list:
                    print(num1 * num2)
                elif operator in div_list:
                    print(num1 / num2)
                else:
                    print("operation coming soon...")
            except Exception as error:
                # print(i, error)
                continue



