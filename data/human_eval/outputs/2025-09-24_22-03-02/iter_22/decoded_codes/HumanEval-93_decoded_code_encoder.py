def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for index in range(len(vowels)):
        letter = vowels[index]
        ascii_value = ord(letter)
        replacement_ascii = ascii_value + 2
        replacement_letter = chr(replacement_ascii)
        vowels_replace[letter] = replacement_letter
    message = message.swapcase()
    encoded_message = []
    for index in range(len(message)):
        current_char = message[index]
        if current_char in vowels:
            replacement_char = vowels_replace[current_char]
            encoded_message.append(replacement_char)
        else:
            encoded_message.append(current_char)
    result = ""
    for index in range(len(encoded_message)):
        result += encoded_message[index]
    return result