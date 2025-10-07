def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for letter in vowels:
        vowels_replace[letter] = chr(ord(letter) + 2)
    message = message.swapcase()
    encoded_message = ""
    for character in message:
        if character in vowels:
            encoded_message += vowels_replace[character]
        else:
            encoded_message += character
    return encoded_message