from typing import Literal


def encode_shift(input_string: str) -> str:
    encoded_result = []
    base_code: int = ord('a')
    for char in input_string:
        current_char_code = ord(char)
        offset_value = (current_char_code + 5 - base_code) % 26
        shifted_char_code = offset_value + base_code
        encoded_result.append(chr(shifted_char_code))
    return ''.join(encoded_result)


def decode_shift(input_string: str) -> str:
    decoded_output = []
    lower_bound: int = ord('a')
    for char in input_string:
        ascii_num = ord(char)
        normalized_val = (ascii_num - 5 - lower_bound) % 26
        revert_ascii = normalized_val + lower_bound
        decoded_output.append(chr(revert_ascii))
    return ''.join(decoded_output)