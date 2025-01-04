def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def calculator():
    print("Simple Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nEnter operation or 'exit': ").strip().lower()
        
        if user_input == 'exit':
            print("Calculator exiting... Goodbye!")
            break
        
        if user_input not in ['+', '-', '*', '/', '%', '^', '1', '2', '3', '4', '5', '6']:
            print("Invalid input. Please enter a valid operation.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if user_input in ['+', '1']:
            print(f"Result: {add(num1, num2)}")
        elif user_input in ['-', '2']:
            print(f"Result: {subtract(num1, num2)}")
        elif user_input in ['*', '3']:
            print(f"Result: {multiply(num1, num2)}")
        elif user_input in ['/', '4']:
            print(f"Result: {divide(num1, num2)}")
        elif user_input in ['%', '5']:
            print(f"Result: {modulus(num1, num2)}")
        elif user_input in ['^', '6']:
            print(f"Result: {power(num1, num2)}")

if __name__ == "__main__":
    calculator()

