from art import logo
from os import system
from calculator import *
system('clear')
print(logo)

def calculator():
    result = 0 

    firs_number = float(input("Enter the first number: "))
    operations = {
        "+": add,
        "-": minus,
        "*": multiply,
        "/": divide
    }
    for operation in operations:
        print(operation)


    while True:

        operator = input("Pick the operation: ")  

        second_number = float(input("Enter the next number: "))



        operation_function = operations[operator]
        result = operation_function(firs_number, second_number)
        print(f"{firs_number} + {second_number} = {result}")
        result2 = result
        if input("Type 'y' to continue calculating with 8.0, or type 'n' to start a new calculation:") == "y":
            firs_number = result
            continue
        else:
            system('clear')
            print(logo)
            calculator()

calculator()






