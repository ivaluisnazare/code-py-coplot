# create a code that prompts the console for a string and an integer as input and returns the string repeated the specified number of times.
def repeat_string():
    user_string = input("Enter a string: ")
    try:
        user_integer = int(input("Enter with a integer: "))
    except ValueError:
        print("Invalid input: expected integer. ")
        return

    if user_integer <= 0:
        print("The number must be greater than zero. ")
        return

    repeated_string = " ".join([user_string] * user_integer)

    print("Repeated string: ", repeated_string)

if __name__ == "__main__":
    repeat_string()
