def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for index in range(len(vowels)):
        character = vowels[index]
        ascii_value = ord(character)
        new_character = chr(ascii_value + 2)
        vowels_replace[character] = new_character
    message = message.swapcase()
    result_characters = []
    for index in range(len(message)):
        character = message[index]
        if character in vowels:
            replacement_character = vowels_replace[character]
            result_characters.append(replacement_character)
        else:
            result_characters.append(character)
    result = ""
    for index in range(len(result_characters)):
        result += result_characters[index]
    return result