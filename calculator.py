def calculator():
    while True:
        try:
            num1 = int(input("Enter first number:\n"))
            num2 = int(input("Enter second number:\n"))
        except ValueError:
            print("Invalid numerical input. Please enter numbers only.\n")
            continue

        print("\nAvailable operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        operation = input("Choose an operation (1-4 or name): ").strip().lower()

        if operation in ("1", "addition"):
            result = num1 + num2
        elif operation in ("2", "subtraction"):
            result = num1 - num2
        elif operation in ("3", "multiplication"):
            result = num1 * num2
        elif operation in ("4", "division"):
            if num2 == 0:
                print("Division by zero is not allowed.\n")
                continue
            result = num1 / num2
        else:
            print("Invalid operation.\n")
            continue

        print(f"Result: {result}\n")
        
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            break

calculator()
