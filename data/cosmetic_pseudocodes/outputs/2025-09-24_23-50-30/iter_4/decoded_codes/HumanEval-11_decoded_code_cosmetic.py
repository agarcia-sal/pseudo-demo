from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        return '1' if char_m != char_n else '0'

    def recurse(index: int, acc: str) -> str:
        if index == len(string_a):
            return acc
        return recurse(index + 1, acc + xor(string_a[index], string_b[index]))

    return recurse(0, '')