def reverse_string():
    user_input = input("Please enter any text: ")
    reversed_output = ""
    for character in user_input:
        reversed_output = character + reversed_output
    return reversed_output

print(reverse_string())