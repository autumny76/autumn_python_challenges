# Go through each of the letters in the message.abs

def caeser_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # runs through characters to identify letters
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            # does the math to shift the letters up to 26
            shifted_value = (ord(char) - base + shift) % 26
            new_char = chr(base + shifted_value)
            result += new_char
            # else prints the character entered
        else:
            result += char
    return result

print(caeser_cipher("happy snowy day", 3))
print(caeser_cipher("happy snowy day", 8))
print(caeser_cipher("happy snowy day", 12))
print(caeser_cipher("it's a snowy day!", 7))