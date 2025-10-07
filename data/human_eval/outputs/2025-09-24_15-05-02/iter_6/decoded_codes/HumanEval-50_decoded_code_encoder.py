def encode_shift(input_string):
    encoded_characters = []
    for character in input_string:
        shifted_code = ((ord(character) + 5 - ord('a')) % 26) + ord('a')
        encoded_characters.append(chr(shifted_code))
    return ''.join(encoded_characters)


def decode_shift(encoded_string):
    decoded_characters = []
    for character in encoded_string:
        shifted_code = ((ord(character) - 5 - ord('a')) % 26) + ord('a')
        decoded_characters.append(chr(shifted_code))
    return ''.join(decoded_characters)