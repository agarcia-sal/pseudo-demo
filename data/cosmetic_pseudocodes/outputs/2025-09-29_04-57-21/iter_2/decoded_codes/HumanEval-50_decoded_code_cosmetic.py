from typing import Literal


def encode_shift(input_string: str) -> str:
    result_string = []
    base_ascii: int = ord("a")
    for idx in range(len(input_string)):
        curr_char_code: int = ord(input_string[idx])
        shifted_index: int = ((curr_char_code - base_ascii) + 5) % 26
        new_char_code: int = shifted_index + base_ascii
        result_string.append(chr(new_char_code))
    return "".join(result_string)


def decode_shift(input_string: str) -> str:
    output = []
    start_val: int = ord("a")
    for position in range(len(input_string)):
        code_point: int = ord(input_string[position])
        adjusted_value: int = ((code_point - start_val) - 5 + 26) % 26
        decoded_char_code: int = start_val + adjusted_value
        output.append(chr(decoded_char_code))
    return "".join(output)