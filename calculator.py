def advanced_calculator():
    print("\n=== Advanced Calculator ===")
    print("Available operations:")
    print("1. Basic Operations (+, -, *, /)")
    print("2. Power (^)")
    print("3. Square root (sqrt)")
    print("4. Percentage (%)")
    print("5. Exit")

    while True:
        try:
            choice = input("\nChoose operation (1-5): ")

            # Exit condition
            if choice == '5':
                print("Thank you for using the calculator!")
                break

            # Square root operation
            if choice == '3':
                num = float(input("Enter number: "))
                if num < 0:
                    print("Error: Cannot calculate square root of negative number")
                else:
                    result = num ** 0.5
                    print(f"Square root of {num} = {result}")
                continue

            # Other operations
            num1 = float(input("Enter first number: "))
            
            # For operations that need two numbers
            if choice in ['1', '2']:
                operator = input("Enter operator: ")
                num2 = float(input("Enter second number: "))

                if choice == '1':  # Basic operations
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/':
                        if num2 == 0:
                            print("Error: Cannot divide by zero")
                            continue
                        result = num1 / num2
                    else:
                        print("Invalid operator")
                        continue

                elif choice == '2':  # Power
                    result = num1 ** num2

            # Percentage calculation
            elif choice == '4':
                result = num1 / 100
                print(f"{num1}% = {result}")
                continue

            else:
                print("Invalid choice")
                continue

            # Print result
            if choice in ['1', '2']:
                print(f"Result: {num1} {operator if choice == '1' else '^'} {num2} = {result}")

        except ValueError:
            print("Error: Please enter valid numbers")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Ask if user wants to perform another calculation
        if input("\nPerform another calculation? (yes/no): ").lower() != "yes":
            print("Thank you for using the calculator!")
            break

# Run the calculator
advanced_calculator()