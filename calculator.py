from art import logo
def add(n1, n2):
    return n1 + n2

def subtrack(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtrack,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = int(input("First number : "))
    for i in operations:
        print(i)

    game = True
    while game:
        
        operation_symbol = input("Pick an operation from the line above : ")
        
        num2 = int(input("what next number : "))
        hasil = operations[operation_symbol]
        jawaban = hasil(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {jawaban}")

        continue_calc = input(f"Type 'y' to continue calculating with {jawaban}, or type 'n' for new calculator : ")
        
        if continue_calc == "y":
            num1 = jawaban
        elif continue_calc == "exit":
            game = False
        else:
            game = False
            calculator()


calculator()