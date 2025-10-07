def encode(message: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_replace = {}
    index = 0
    while index < len(vowels):
        vowel_char = vowels[index]
        vowel_char_code = ord(vowel_char)
        replacement_char_code = vowel_char_code + 2
        replacement_char = chr(replacement_char_code)
        vowels_replace[vowel_char] = replacement_char
        index += 1
    message = message.swapcase()
    result_chars = []
    index = 0
    while index < len(message):
        current_char = message[index]
        if current_char in vowels:
            append_char = vowels_replace[current_char]
        else:
            append_char = current_char
        result_chars.append(append_char)
        index += 1
    encoded_message = ''.join(result_chars)
    return encoded_message