#crie um código que receba dois dados de quaisquer tipo do usuário no console e concatene-os em uma única string.
def concatenate_user_input():
    data1 = input("Digite o primeiro dado: ")
    data2 = input("Digite o segundo dado: ")

    concatenated_string = str(data1) + str(data2)

    print("Dados concatenados:", concatenated_string)

if __name__ == "__main__":
    concatenate_user_input()




