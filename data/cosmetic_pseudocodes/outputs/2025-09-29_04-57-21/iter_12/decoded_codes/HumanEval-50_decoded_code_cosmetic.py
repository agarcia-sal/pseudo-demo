from typing import List


def encode_shift(input_string: str) -> str:
    output_chars: List[str] = []
    idx: int = 0
    while idx < len(input_string):
        current_char: str = input_string[idx]
        ascii_val: int = ord(current_char)
        shifted_val: int = ((ascii_val - ord('a') + 5) % 26) + ord('a')
        new_char: str = chr(shifted_val)
        output_chars.append(new_char)
        idx += 1
    return ''.join(output_chars)


def decode_shift(input_string: str) -> str:
    result_chars: List[str] = []
    position: int = 0
    while position < len(input_string):
        char_at_pos: str = input_string[position]
        ascii_code: int = ord(char_at_pos)
        adjusted_code: int = ((ascii_code - ord('a') - 5) % 26) + ord('a')
        decoded_char: str = chr(adjusted_code)
        result_chars.append(decoded_char)
        position += 1
    return ''.join(result_chars)