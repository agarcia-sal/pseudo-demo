from typing import List

def encode_shift(input_string: str) -> str:
    result_buffer: List[str] = []
    position_index: int = 0
    base: int = ord('a')

    while position_index < len(input_string):
        current_char = input_string[position_index]
        ascii_code = ord(current_char)
        shifted_code = ((ascii_code + 5) - base) % 26
        shifted_code += base
        result_buffer.append(chr(shifted_code))
        position_index += 1

    return "".join(result_buffer)


def decode_shift(input_string: str) -> str:
    output_chars: List[str] = []
    index_counter: int = 0
    base_value: int = ord('a')

    while index_counter < len(input_string):
        symbol = input_string[index_counter]
        code_value = ord(symbol)
        adjusted_value = ((code_value - 5) - base_value) % 26
        adjusted_value += base_value
        output_chars.append(chr(adjusted_value))
        index_counter += 1

    return "".join(output_chars)