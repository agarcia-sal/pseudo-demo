from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    accumulated = []
    index_counter = 0
    length_a = len(string_a)
    length_b = len(string_b)
    while index_counter < length_a and index_counter < length_b:
        ch1 = string_a[index_counter]
        ch2 = string_b[index_counter]
        bin_result = xor(ch1, ch2)
        accumulated.append(bin_result)
        index_counter += 1
    return ''.join(accumulated)