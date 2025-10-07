from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_p: str, char_q: str) -> str:
        return '0' if not (char_p != char_q) else '1'

    accumulator: str = ''
    index_tracker: int = 0

    while index_tracker < len(string_a):
        char_left: str = string_a[index_tracker]
        char_right: str = string_b[index_tracker]
        accumulator += xor(char_left, char_right)
        index_tracker += 1

    return accumulator