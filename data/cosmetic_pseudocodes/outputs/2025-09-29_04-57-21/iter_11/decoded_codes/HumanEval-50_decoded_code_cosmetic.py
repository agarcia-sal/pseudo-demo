from typing import List

def encode_shift(input_string: str) -> str:
    result_string = []
    idx = 0
    while idx < len(input_string):
        current_char = input_string[idx]
        ascii_code = ord(current_char)
        shifted_value = ((ascii_code - ord('a')) + 5) % 26
        encoded_char = chr(shifted_value + ord('a'))
        result_string.append(encoded_char)
        idx += 1
    return ''.join(result_string)

def decode_shift(input_string: str) -> str:
    accumulator = []
    position = 0
    while position < len(input_string):
        symbol = input_string[position]
        code_num = ord(symbol)
        adjusted_num = ((code_num - ord('a')) - 5 + 26) % 26
        decoded_symbol = chr(adjusted_num + ord('a'))
        accumulator.append(decoded_symbol)
        position += 1
    return ''.join(accumulator)