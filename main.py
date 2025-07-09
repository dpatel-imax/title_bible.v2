print("Simple Calculator")
print("Choose an operation:")
print(" + for addition")
print(" - for subtraction")
print(" * for multiplication")
print(" / for division")
print(" ** for exponentiation")
operation = input("Enter operation (+, -, *, /, **): ")
if operation not in {"+", "-", "*", "/", "**"}:
    print("Unsupported operation.")
else:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "**":
            result = num1 ** num2
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
