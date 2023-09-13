#python program for calculator
def add (n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
   return n1 / n2
def perform_calculation(n1, n2, operation):
    if operation == "+":
        return add(n1,n2)
    elif operation == "-":
        return sub(n1,n2)
    elif operation == "*":
        return mul(n1,n2)
    elif operation == "/":
        # Check for division by zero
        if n2 != 0:
            return div(n1,n2)
        else:
            return "cannot divide by zero"
    else:
        return "Invalid operation"

try:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    result = perform_calculation(n1, n2, operation)
    print("Result:",result)
except :
    print("Invalid input. Please enter valid numbers.")




