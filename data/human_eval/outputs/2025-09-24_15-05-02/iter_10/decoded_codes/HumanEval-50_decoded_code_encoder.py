def encode_shift(input_string):
    encoded_string = ''
    for character in input_string:
        shifted_value = ((ord(character) + 5 - ord('a')) % 26) + ord('a')
        encoded_character = chr(shifted_value)
        encoded_string += encoded_character
    return encoded_string

def decode_shift(input_string):
    decoded_string = ''
    for character in input_string:
        shifted_value = ((ord(character) - 5 - ord('a')) % 26) + ord('a')
        decoded_character = chr(shifted_value)
        decoded_string += decoded_character
    return decoded_string