def encode_shift(input_string: str) -> str:
    encoded_characters = []
    for character in input_string:
        shifted_value = ((ord(character) + 5 - ord('a')) % 26) + ord('a')
        encoded_characters.append(chr(shifted_value))
    encoded_string = ''.join(encoded_characters)
    return encoded_string


def decode_shift(input_string: str) -> str:
    decoded_characters = []
    for character in input_string:
        shifted_value = ((ord(character) - 5 - ord('a')) % 26) + ord('a')
        decoded_characters.append(chr(shifted_value))
    decoded_string = ''.join(decoded_characters)
    return decoded_string