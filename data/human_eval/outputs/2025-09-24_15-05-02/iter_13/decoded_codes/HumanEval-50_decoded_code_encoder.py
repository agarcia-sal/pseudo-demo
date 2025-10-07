def encode_shift(string_s):
    encoded_characters = []
    for ch in string_s:
        shifted_value = ((ord(ch) + 5 - ord("a")) % 26) + ord("a")
        shifted_character = chr(shifted_value)
        encoded_characters.append(shifted_character)
    encoded_string = "".join(encoded_characters)
    return encoded_string

def decode_shift(string_s):
    decoded_characters = []
    for ch in string_s:
        shifted_value = ((ord(ch) - 5 - ord("a")) % 26) + ord("a")
        shifted_character = chr(shifted_value)
        decoded_characters.append(shifted_character)
    decoded_string = "".join(decoded_characters)
    return decoded_string