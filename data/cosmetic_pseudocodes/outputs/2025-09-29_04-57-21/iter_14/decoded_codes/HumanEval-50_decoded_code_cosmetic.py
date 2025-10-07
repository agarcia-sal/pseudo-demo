from typing import List

def encode_shift(input_string: str) -> str:
    transformed_chars: List[str] = []
    index: int = 0
    base_offset: int = ord('a')
    length: int = len(input_string)
    while index < length:
        ascii_value: int = ord(input_string[index])
        shuffled_value: int = (((ascii_value + 5) - base_offset) % 26) + base_offset
        transformed_chars.append(chr(shuffled_value))
        index += 1
    return ''.join(transformed_chars)

def decode_shift(input_string: str) -> str:
    output_collection: List[str] = []
    position: int = 0
    zero_point: int = ord('a')
    length: int = len(input_string)
    while position < length:
        char_code: int = ord(input_string[position])
        adjusted_code: int = (((char_code - 5) - zero_point) % 26) + zero_point
        output_collection.append(chr(adjusted_code))
        position += 1
    return ''.join(output_collection)