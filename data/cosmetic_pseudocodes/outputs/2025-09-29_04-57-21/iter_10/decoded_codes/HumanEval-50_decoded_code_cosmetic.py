from typing import List

def encode_shift(input_string: str) -> str:
    result_chars: List[str] = []
    index: int = 0
    base_val: int = ord('a')
    length: int = len(input_string)
    while index < length:
        current_char: str = input_string[index]
        shifted_num: int = ((ord(current_char) - base_val + 5) % 26) + base_val
        result_chars.append(chr(shifted_num))
        index += 1
    return ''.join(result_chars)

def decode_shift(input_string: str) -> str:
    output_chars: List[str] = []
    pos: int = 0
    offset: int = ord('a')
    length: int = len(input_string)
    while pos < length:
        letter: str = input_string[pos]
        adjusted_val: int = ((ord(letter) - offset - 5) % 26) + offset
        output_chars.append(chr(adjusted_val))
        pos += 1
    return ''.join(output_chars)