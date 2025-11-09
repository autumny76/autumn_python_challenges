def is_palindrome():
    user_input = input("Please enter your text here: ").lower().replace(" ", "")
    reversed_text = ""
    for char in user_input:
        reversed_text = char + reversed_text
    if user_input == reversed_text:
        print("True, this is a palendrome")
    else:
        print("False, this is not a palindrome")
   
    return reversed_text

print(is_palindrome())