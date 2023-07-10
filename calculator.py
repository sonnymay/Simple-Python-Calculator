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
        return "Error: Division by zero is not allowed"

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def modulo(x, y):
    return x % y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square root")
    print("7. Modulo")

    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice == '6':
        num1 = float(input("Enter number: "))
        print(f"Square root of {num1} = {square_root(num1)}")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '7':
            print(f"{num1} mod {num2} = {modulo(num1, num2)}")
        else:
            print("Invalid input")

if __name__ == "__main__":
    calculator()
