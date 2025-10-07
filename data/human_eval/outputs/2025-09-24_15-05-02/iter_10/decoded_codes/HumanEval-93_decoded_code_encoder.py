def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for vowel_character in vowels:
        vowels_replace[vowel_character] = chr(ord(vowel_character) + 2)
    message = message.swapcase()
    encoded_message = []
    for character in message:
        if character in vowels_replace:
            encoded_message.append(vowels_replace[character])
        else:
            encoded_message.append(character)
    return "".join(encoded_message)