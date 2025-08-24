import math

def calculator():
    print("=== Advanced Calculator ===")
    print("Operations: +, -, *, /, ** (power), sqrt")
    print("Type 'q' to quit")

    while True:
        op = input("\nEnter operator: ")

        if op == 'q':
            print("Goodbye!")
            break

        if op == 'sqrt':
            num = float(input("Enter number: "))
            print("Result:", math.sqrt(num))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if op == '+':
                print("Result:", num1 + num2)
            elif op == '-':
                print("Result:", num1 - num2)
            elif op == '*':
                print("Result:", num1 * num2)
            elif op == '/':
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Cannot divide by zero")
            elif op == '**':
                print("Result:", num1 ** num2)
            else:
                print("Invalid operator")

calculator()
