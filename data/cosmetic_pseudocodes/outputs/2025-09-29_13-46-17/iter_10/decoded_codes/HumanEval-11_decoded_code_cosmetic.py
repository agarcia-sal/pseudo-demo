from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:

    def xor(character_i: str, character_j: str) -> str:
        if not (character_i != character_j):
            return '0'
        else:
            return '1'

    def fold_zip(s1: str, s2: str, acc: str) -> str:
        if not s1 or not s2:
            return acc
        x = xor(s1[0], s2[0])
        return fold_zip(s1[1:], s2[1:], acc + x)

    result = fold_zip(string_a, string_b, '')
    return result