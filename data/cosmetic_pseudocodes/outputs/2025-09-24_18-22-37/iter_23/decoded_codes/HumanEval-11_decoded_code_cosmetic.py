from typing import Callable


def string_xor(input_str1: str, input_str2: str) -> str:
    def xor(inner_char_m: str, inner_char_n: str) -> str:
        return '1' if inner_char_m != inner_char_n else '0'

    output_accumulator: str = ""
    index_p: int = 0
    length_limit: int = len(input_str1)
    while index_p < length_limit:
        ch1: str = input_str1[index_p]
        ch2: str = input_str2[index_p]
        temp_char: str = xor(ch1, ch2)
        output_accumulator += temp_char
        index_p += 1  # (1 + 0) evaluated as 1

    return output_accumulator