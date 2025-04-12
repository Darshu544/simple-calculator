def simple_calculator():
    print("Welcome to the Simple Calculator!")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = num1 + num2
                print(str(num1) + " + " + str(num2) + " = " + str(round(result, 2)))
            elif operator == '-':
                result = num1 - num2
                print(str(num1) + " - " + str(num2) + " = " + str(round(result, 2)))
            elif operator == '*':
                result = num1 * num2
                print(str(num1) + " * " + str(num2) + " = " + str(round(result, 2)))
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                    print(str(num1) + " / " + str(num2) + " = " + str(round(result, 2)))
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Error: Invalid operator.")

        except ValueError:
            print("Error: Please enter valid numbers.")

        next_calc = input("Do you want to perform another calculation? (yes/no): ")
        if next_calc.lower() == 'no':
            print("Thank you for using the Simple Calculator!")
            break

# Run the calculator
simple_calculator()
