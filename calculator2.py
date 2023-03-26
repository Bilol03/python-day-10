from art import logo
from os import system
from calculator import *
print(logo)
result = 0 






while  True:
    firs_number = float(input("Enter the first number: "))
    operations = {
        "+": add,
        "-": minus,
        "*": multiply,
        "/": divide
    }

    for operation in operations:
        print(operation)

    operator = input("Pick the operation: ")  
    second_number = float(input("Enter the next number: "))

    operation_function = operations[operator]
    result = operation_function(firs_number, second_number)

    print(result)

    play_again = input("Type 'y' to continue calculating with 8.0, or type 'n' to start a new calculation: ")

    if play_again == "n":
        result = 0
        system("clear")
        print(logo)
    else:
        while play_again != "n":
            operations = {
                "+": add,
                "-": minus,
                "*": multiply,
                "/": divide
            }
            for operation in operations:
                print(operation)
            operator = input("Pick the operation: ")  

            second_number = float(input("Enter the next number: "))



            operation_function = operations[operator]
            result = operation_function(result, second_number)

            print(result)
            play_again = input("Type 'y' to continue calculating with 8.0, or type 'n' to start a new calculation: ")
            if play_again != "n":
                continue






