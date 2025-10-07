def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for index in range(len(vowels)):
        character = vowels[index]
        character_code = ord(character)
        replacement_character = chr(character_code + 2)
        vowels_replace[character] = replacement_character
    message = message.swapcase()
    encoded_message_characters = []
    for index in range(len(message)):
        current_character = message[index]
        if current_character in vowels:
            encoded_message_characters.append(vowels_replace[current_character])
        else:
            encoded_message_characters.append(current_character)
    result = "".join(encoded_message_characters)
    return result