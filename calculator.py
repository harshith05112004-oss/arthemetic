"""
Simple Arithmetic Calculator
A basic calculator that performs arithmetic operations.
"""

def add(x, y):
    """Add two numbers."""
    return x + y


def subtract(x, y):
    """Subtract two numbers."""
    return x - y


def multiply(x, y):
    """Multiply two numbers."""
    return x * y


def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def power(x, y):
    """Raise x to the power of y."""
    return x ** y


def main():
    """Main function to run the calculator."""
    print("=" * 50)
    print("        SIMPLE ARITHMETIC CALCULATOR")
    print("=" * 50)
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")
    print("\n" + "=" * 50)

    while True:
        choice = input("\nEnter choice (1/2/3/4/5/6): ").strip()

        if choice == "6":
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice in ("1", "2", "3", "4", "5"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"\n{num1} + {num2} = {add(num1, num2)}")

                elif choice == "2":
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")

                elif choice == "3":
                    print(f"\n{num1} * {num2} = {multiply(num1, num2)}")

                elif choice == "4":
                    print(f"\n{num1} / {num2} = {divide(num1, num2)}")

                elif choice == "5":
                    print(f"\n{num1} ^ {num2} = {power(num1, num2)}")

            except ValueError as e:
                print(f"\nError: {e}")
            except Exception as e:
                print(f"\nError: Invalid input. Please enter valid numbers.")
        else:
            print("\nInvalid choice. Please select 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
