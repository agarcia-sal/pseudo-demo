def encode(message):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowels_replace = {}
    for index in range(len(vowels)):
        current_vowel = vowels[index]
        current_vowel_ascii = ord(current_vowel)
        replacement_ascii = current_vowel_ascii + 2
        replacement_char = chr(replacement_ascii)
        vowels_replace[current_vowel] = replacement_char
    message = message.swapcase()
    encoded_message_chars = []
    for index in range(len(message)):
        current_char = message[index]
        if current_char in vowels:
            encoded_message_chars.append(vowels_replace[current_char])
        else:
            encoded_message_chars.append(current_char)
    encoded_message = "".join(encoded_message_chars)
    return encoded_message