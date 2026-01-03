#write a code that receives an integer input from the console and checks if it is even or odd. Use if/else conditionals to perform the check.
def check_even_odd():
    try:
        user_input = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input: expected an integer.")
        return

    if user_input % 2 == 0:
        print(f"The number {user_input} is even.")
    else:
        print(f"The number {user_input} is odd.")
if __name__ == "__main__":
    check_even_odd()