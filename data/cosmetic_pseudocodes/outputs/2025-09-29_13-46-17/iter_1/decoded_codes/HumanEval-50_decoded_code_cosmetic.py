from typing import Literal


def encode_shift(input_string: str) -> str:
    result_string = []
    ord_a = ord('a')
    for each_char in input_string:
        ascii_val = ord(each_char)
        shifted_val = ((ascii_val + 5) - ord_a) % 26 + ord_a
        result_string.append(chr(shifted_val))
    return ''.join(result_string)


def decode_shift(input_string: str) -> str:
    decoded_string = []
    ord_a = ord('a')
    for each_char in input_string:
        ascii_val = ord(each_char)
        shifted_val = ((ascii_val - 5) - ord_a) % 26 + ord_a
        decoded_string.append(chr(shifted_val))
    return ''.join(decoded_string)