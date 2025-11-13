# calculator.py
# Python Developer Internship - Task 1
# Author: Nagendra
# Description: Command-line Calculator App supporting +, -, *, /

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def calculator():
    print("🔹 Welcome to CLI Calculator 🔹")
    print("Available operations: +, -, *, /")
    print("Type 'exit' anytime to quit.\n")

    while True:
        operation = input("Enter operation (+, -, *, / or 'exit'): ").strip().lower()

        if operation == "exit":
            print("👋 Exiting calculator. Goodbye!")
            break

        if operation not in ['+', '-', '*', '/']:
            print("❌ Invalid operation! Please choose +, -, *, /")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Please enter valid numeric values.")
            continue

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"✅ Result: {result}\n")

if __name__ == "__main__":
    calculator()
