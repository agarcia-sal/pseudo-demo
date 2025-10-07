def encode_shift(s: str):
    encoded_characters = []
    for index in range(len(s)):
        ch = s[index]
        original_code = ord(ch)
        shifted_code = original_code + 5 - ord("a")
        modulo_code = shifted_code % 26
        final_code = modulo_code + ord("a")
        encoded_character = chr(final_code)
        encoded_characters.append(encoded_character)
    encoded_string = ""
    for index in range(len(encoded_characters)):
        encoded_string += encoded_characters[index]
    return encoded_string

def decode_shift(s: str):
    decoded_characters = []
    for index in range(len(s)):
        ch = s[index]
        original_code = ord(ch)
        shifted_code = original_code - 5 - ord("a")
        modulo_code = shifted_code % 26
        final_code = modulo_code + ord("a")
        decoded_character = chr(final_code)
        decoded_characters.append(decoded_character)
    decoded_string = ""
    for index in range(len(decoded_characters)):
        decoded_string += decoded_characters[index]
    return decoded_string