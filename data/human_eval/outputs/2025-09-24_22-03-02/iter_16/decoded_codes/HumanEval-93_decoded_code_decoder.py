def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for i in vowels:
        unicode_value = ord(i)
        replacement_unicode = unicode_value + 2
        replacement_char = chr(replacement_unicode)
        vowels_replace[i] = replacement_char
    message = message.swapcase()
    encoded_message_chars = []
    for i in message:
        if i in vowels_replace:
            encoded_message_chars.append(vowels_replace[i])
        else:
            encoded_message_chars.append(i)
    encoded_message = "".join(encoded_message_chars)
    return encoded_message