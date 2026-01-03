# Write a code that receives two numbers as input in the terminal, as well as the type of operation (addition, subtraction, multiplication or division) performs the requested operation between the numbers, and then displays the expected result.
def simple_operations():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input: expected a number.")
        return

    operation = input("Enter the operation (addition, subtraction, multiplication, division): ").strip().lower()

    if operation == "addition":
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is: {result}")
    elif operation == "subtraction":
        result = num1 - num2
        print(f"The result of subtracting {num2} from {num1} is: {result}")
    elif operation == "multiplication":
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is: {result}")
    elif operation == "division":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    else:
        print("Invalid operation. Please choose from addition, subtraction, multiplication, or division.")
if __name__ == "__main__":
    simple_operations()
