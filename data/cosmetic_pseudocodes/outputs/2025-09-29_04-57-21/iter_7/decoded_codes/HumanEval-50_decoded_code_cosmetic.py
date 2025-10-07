from typing import Literal


def encode_shift(input_string: str) -> str:
    result = []
    for ch in input_string:
        ascii_num = ord(ch)
        shifted_num = ((ascii_num + 5 - ord('a')) % 26) + ord('a')
        encoded_ch = chr(shifted_num)
        result.append(encoded_ch)
    return ''.join(result)


def decode_shift(input_string: str) -> str:
    output = []
    for current_char in input_string:
        val = ord(current_char)
        diff = val - 5
        normalized = (diff - ord('a')) % 26
        final_val = normalized + ord('a')
        decoded_char = chr(final_val)
        output.append(decoded_char)
    return ''.join(output)