from typing import Callable


def encode_shift(input_string: str) -> str:
    def shift_character(c: str) -> str:
        base_code = ord("a")
        original_code = ord(c)
        offset_code = ((original_code + 5) - base_code) % 26
        adjusted_code = offset_code + base_code
        return chr(adjusted_code)

    encoded_result = ''.join(shift_character(letter) for letter in input_string)
    return encoded_result


def decode_shift(input_string: str) -> str:
    def unshift_character(c: str) -> str:
        base_code = ord("a")
        original_code = ord(c)
        offset_code = ((original_code - 5) - base_code) % 26
        adjusted_code = offset_code + base_code
        return chr(adjusted_code)

    decoded_result = ''.join(unshift_character(letter) for letter in input_string)
    return decoded_result