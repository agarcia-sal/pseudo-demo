def encode(message: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_replace = {}
    for i in vowels:
        vowels_replace[i] = chr(ord(i) + 2)
    message = message.swapcase()
    encoded_characters = []
    for character in message:
        if character in vowels:
            encoded_characters.append(vowels_replace[character])
        else:
            encoded_characters.append(character)
    encoded_message = ''.join(encoded_characters)
    return encoded_message