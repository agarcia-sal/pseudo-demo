from typing import Literal

def encode_shift(input_string: str) -> str:
    result_string = []
    index = 0
    while index < len(input_string):
        current_char = input_string[index]
        ascii_num = ord(current_char)
        shifted_num = ((ascii_num - ord('a')) + 5) % 26
        new_char = chr(shifted_num + ord('a'))
        result_string.append(new_char)
        index += 1
    return ''.join(result_string)

def decode_shift(input_string: str) -> str:
    accumulator = []
    pointer = 0
    while pointer < len(input_string):
        ch = input_string[pointer]
        base_val = ord(ch)
        adjusted_val = ((base_val - ord('a')) - 5) % 26
        decoded_char = chr(adjusted_val + ord('a'))
        accumulator.append(decoded_char)
        pointer += 1
    return ''.join(accumulator)