import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square_root(x):
    return math.sqrt(x)

def modulo(x, y):
    return x % y

print("\n-----Simple Calculator-----\n")
print("Enter 'exit' or '=' to quit")

result = None

while True:
    if result is None:
        num1 = float(input("Enter a number: "))
    else:
        num1 = result
    
    operator = input("Enter an operator (+, -, *, /, sqrt, %, =): ")
    
    if operator in ("exit", "="):
        break
    
    if operator in ("+", "-", "*", "/", "%"):
        num2 = float(input("Enter another number: "))
    
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    elif operator == "sqrt":
        result = square_root(num1)
    elif operator == "%":
        result = modulo(num1, num2)
    
    print("Result:", result)

print("\n-----Calculator Closed-----\n")
