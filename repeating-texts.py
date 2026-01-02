# create a code that prompts the console for a string and an integer as input and returns the string repeated the specified number of times.
def repeat_string():
    user_string = input("Digite uma string: ")
    try:
        user_integer = int(input("Digite um inteiro: "))
    except ValueError:
        print("Entrada inválida: inteiro esperado.")
        return

    if user_integer <= 0:
        print("O número deve ser maior que zero.")
        return

    repeated_string = " ".join([user_string] * user_integer)

    print("String repetida:", repeated_string)

if __name__ == "__main__":
    repeat_string()
