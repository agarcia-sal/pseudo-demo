from typing import Literal


def encode_shift(input_string: str) -> str:
    result_string = []
    base_value = ord('a')
    for current_char in input_string:
        ascii_equivalent = ((ord(current_char) + 5 - base_value) % 26) + base_value
        encoded_char = chr(ascii_equivalent)
        result_string.append(encoded_char)
    return ''.join(result_string)


def decode_shift(input_string: str) -> str:
    output = []
    base_ascii = ord('a')
    for char_element in input_string:
        shifted_value = ((ord(char_element) - 5 - base_ascii) % 26) + base_ascii
        decoded_char = chr(shifted_value)
        output.append(decoded_char)
    return ''.join(output)