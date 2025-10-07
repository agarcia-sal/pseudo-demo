def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for index in range(len(vowels)):
        character = vowels[index]
        new_char_code = ord(character) + 2
        new_char = chr(new_char_code)
        vowels_replace[character] = new_char
    message = message.swapcase()
    encoded_characters = []
    for index in range(len(message)):
        character = message[index]
        if character in vowels:
            encoded_characters.append(vowels_replace[character])
        else:
            encoded_characters.append(character)
    encoded_message = ""
    for index in range(len(encoded_characters)):
        encoded_message += encoded_characters[index]
    return encoded_message