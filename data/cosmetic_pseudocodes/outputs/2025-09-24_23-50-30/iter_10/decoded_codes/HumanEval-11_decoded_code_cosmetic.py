from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_p: str, char_q: str) -> str:
        return '0' if char_p == char_q else '1'

    accumulator: str = ""
    index_counter: int = 0

    while index_counter < len(string_a) and index_counter < len(string_b):
        accumulator += xor(string_a[index_counter], string_b[index_counter])
        index_counter += 1

    return accumulator