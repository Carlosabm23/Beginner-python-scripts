def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

operations_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}

"""
one way of doing this or you can use a while loop and function

"""
# num1 = float(input("What Is Your First Number? \n"))
# for symbol in operations_dict:
#     print(symbol)
# operation_symbol = input("What Operation do you want to do? \n")
# num2 = float(input("What Is Your Second Number? \n"))
# answer = operations_dict[operation_symbol](num1,num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")
# choice = input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
#
# if choice == 'y':
#     num1 = answer
#     for symbol in operations_dict:
#         print(symbol)
#     operation_symbol = input("What Operation do you want to do? \n")
#     num2 = float(input("What Is Your Second Number? \n"))
#     answer2 = operations_dict[operation_symbol](num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer2}")
#     choice = input(f"Type 'Y' to continue calculating with {answer2}, or type 'n' to start a new calculation: ").lower()
# else:
#     print("Father Help")


def calculate():

    keep_mathing = True
    num1 = float(input("What Is Your First Number? \n"))


    while keep_mathing:
        for symbol in operations_dict:
            print(symbol)
        operation_symbol = input("What Operation do you want to do? \n")
        num2 = float(input("What Is Your Second Number? \n"))
        answer = operations_dict[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice == 'y':
            num1 = answer
        else:
            keep_mathing = False
            print("\n" * 50)
            calculate()

calculate()






