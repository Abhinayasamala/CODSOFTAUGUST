#python program for calculator
#function to addition of two numbers
def add (n1,n2):
    return n1 + n2
#function to subtraction of two numbers
def sub(n1,n2):
    return n1 - n2
#function to multiplication of two numbers
def mul(n1,n2):
    return n1 * n2
#function to division of two numbers
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

# Prompt the user for input
try:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    # Perform the calculation
    result = perform_calculation(n1, n2, operation)
    # Display the result
    print("Result:",result)
except :
    print("Invalid input. Please enter valid numbers.")


