from typing import Callable


def string_xor(string_m: str, string_n: str) -> str:
    def inner_xor(char_p: str, char_q: str) -> str:
        return '0' if char_p == char_q else '1'

    accum: str = ''
    index_var: int = 0
    while index_var < len(string_m):
        accum += inner_xor(string_m[index_var], string_n[index_var])
        index_var += 1
    return accum