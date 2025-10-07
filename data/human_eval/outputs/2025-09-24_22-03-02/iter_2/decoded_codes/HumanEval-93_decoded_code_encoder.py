def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for character in vowels:
        vowels_replace[character] = chr(ord(character) + 2)
    message = message.swapcase()
    encoded_message = ""
    for character in message:
        if character in vowels_replace:
            encoded_message += vowels_replace[character]
        else:
            encoded_message += character
    return encoded_message