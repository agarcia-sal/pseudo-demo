def encode(message) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    index = 0
    while index < len(vowels):
        current_char = vowels[index]
        ascii_value = ord(current_char)
        replaced_char = chr(ascii_value + 2)
        vowels_replace[current_char] = replaced_char
        index += 1
    message = message.swapcase()
    encoded_message_characters = []
    index = 0
    while index < len(message):
        current_char = message[index]
        if current_char in vowels_replace:
            replaced_char = vowels_replace[current_char]
            encoded_message_characters.append(replaced_char)
        else:
            encoded_message_characters.append(current_char)
        index += 1
    encoded_message = "".join(encoded_message_characters)
    return encoded_message