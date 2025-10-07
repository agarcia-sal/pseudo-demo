from typing import Callable

def encode_shift(input_string: str) -> str:
    def helper_shift(s: str, index: int, acc: str) -> str:
        if index == len(s):
            return acc
        current_char_code = ord(s[index])
        shifted_code = ((current_char_code - ord('a') + 5) % 26) + ord('a')
        new_acc = acc + chr(shifted_code)
        return helper_shift(s, index + 1, new_acc)
    return helper_shift(input_string, 0, "")

def decode_shift(input_string: str) -> str:
    result_str = ""
    i = 0
    while i < len(input_string):
        char_value = ord(input_string[i])
        adjusted_val = ord('a') + ((char_value - ord('a') - 5 + 26) % 26)
        decoded_char = chr(adjusted_val)
        result_str += decoded_char
        i += 1
    return result_str