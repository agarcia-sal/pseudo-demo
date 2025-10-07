def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for index in range(len(vowels)):
        i = vowels[index]
        character_code = ord(i)
        new_character_code = character_code + 2
        new_character = chr(new_character_code)
        vowels_replace[i] = new_character
    message = message.swapcase()
    encoded_characters = []
    for index in range(len(message)):
        i = message[index]
        if i in vowels:
            encoded_characters.append(vowels_replace[i])
        else:
            encoded_characters.append(i)
    result = "".join(encoded_characters)
    return result