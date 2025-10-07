from typing import Callable


def encode_shift(input_string: str) -> str:
    def helper(position: int) -> str:
        if position == len(input_string):
            return ""
        symbol = chr(((ord(input_string[position]) - ord('a') + 5) % 26) + ord('a'))
        return symbol + helper(position + 1)

    return helper(0)


def decode_shift(input_string: str) -> str:
    def recursive_decode(index: int) -> str:
        if index >= len(input_string):
            return ""
        curr_code = ord(input_string[index]) - ord('a') - 5
        adjusted_code = ((curr_code % 26) + 26) % 26
        letter = chr(adjusted_code + ord('a'))
        return letter + recursive_decode(index + 1)

    return recursive_decode(0)