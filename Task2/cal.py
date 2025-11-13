# calculator.py
# Python Developer Internship - Task 1 (Enhanced Version)
# Author: <Your Name>
# Description: Interactive CLI Calculator with history and modular design

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers with zero-check."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Dictionary mapping operation numbers to functions
operations = {
    1: ("Addition", add),
    2: ("Subtraction", subtract),
    3: ("Multiplication", multiply),
    4: ("Division", divide)
}

def display_menu():
    """Display operation menu."""
    print("\n🔹 Calculator Menu 🔹")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("5. View Calculation History")
    print("6. Exit")

def get_number(prompt):
    """Safely get a float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Invalid input! Please enter a numeric value.")

def calculator():
    """Main calculator loop."""
    history = []
    print("Welcome to the Interactive Python CLI Calculator 🧮")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '6':
            print("👋 Exiting Calculator. Goodbye!")
            break
        elif choice == '5':
            print("\n📜 Calculation History:")
            if not history:
                print("No calculations yet.")
            else:
                for i, entry in enumerate(history, start=1):
                    print(f"{i}. {entry}")
            continue

        # Validate choice
        if not choice.isdigit() or int(choice) not in operations:
            print("❌ Invalid choice! Please select a valid option (1-6).")
            continue

        choice = int(choice)
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operation_name, func = operations[choice]
        result = func(num1, num2)
        output = f"{operation_name}: {num1} and {num2} → Result = {result}"
        print(f"✅ {output}")

        # Save to history
        history.append(output)

if __name__ == "__main__":
    calculator()
