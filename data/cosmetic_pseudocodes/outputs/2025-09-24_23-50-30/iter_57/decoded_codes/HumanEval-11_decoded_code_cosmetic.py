from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        return '1' if character_p != character_q else '0'

    accumulator = []
    index_counter = 0
    max_len = min(len(string_a), len(string_b))
    while index_counter < max_len:
        char_m = string_a[index_counter]
        char_n = string_b[index_counter]
        accumulator.append(xor(char_m, char_n))
        index_counter += 1
    return ''.join(accumulator)