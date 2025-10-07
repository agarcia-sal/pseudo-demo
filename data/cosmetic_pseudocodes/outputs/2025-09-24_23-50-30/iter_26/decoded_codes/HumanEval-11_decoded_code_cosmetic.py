from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_p: str, char_q: str) -> str:
        if char_p == char_q:
            return '0'
        else:
            return '1'

    def helper(index_k: int, accumulator_m: str) -> str:
        if index_k == len(string_a):
            return accumulator_m
        return helper(index_k + 1, accumulator_m + xor(string_a[index_k], string_b[index_k]))

    return helper(0, "")