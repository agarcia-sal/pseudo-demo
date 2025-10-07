def encode_shift(string_input):
    encoded_characters = []
    for character in string_input:
        shifted_value = ((ord(character) + 5 - ord("a")) % 26) + ord("a")
        encoded_characters.append(chr(shifted_value))
    encoded_string = "".join(encoded_characters)
    return encoded_string

def decode_shift(string_input):
    decoded_characters = []
    for character in string_input:
        shifted_value = ((ord(character) - 5 - ord("a")) % 26) + ord("a")
        decoded_characters.append(chr(shifted_value))
    decoded_string = "".join(decoded_characters)
    return decoded_string