from typing import Callable

def encode_shift(input_string: str) -> str:
    def helper(index: int) -> str:
        if index == len(input_string):
            return ""
        ch_code = ord(input_string[index])
        shifted_code = ((ch_code - ord("a") + 5) % 26) + ord("a")
        return chr(shifted_code) + helper(index + 1)
    return helper(0)

def decode_shift(input_string: str) -> str:
    def decode_recursive(pos: int) -> str:
        if pos >= len(input_string):
            return ""
        val = ord(input_string[pos])
        new_val = ((val - ord("a") - 5 + 26) % 26) + ord("a")
        return chr(new_val) + decode_recursive(pos + 1)
    return decode_recursive(0)