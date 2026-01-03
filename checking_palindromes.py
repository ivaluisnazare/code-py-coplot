# write code to test if a word typed into the console is a palindrome. Use string manipulation concepts to reverse the word and compare it to the original.
def check_palindrome():
    user_input = input("Enter a word: ")
    cleaned_input = ''.join(char.lower() for char in user_input if char.isalnum())
    reversed_input = cleaned_input[::-1]

    if cleaned_input == reversed_input:
        print(f"The word '{user_input}' is a palindrome.")
    else:
        print(f"The word '{user_input}' is not a palindrome.")
if __name__ == "__main__":
    check_palindrome()
