from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    def build_result(index: int, accumulated: str) -> str:
        if index >= len(string_a):
            return accumulated
        next_char = xor(string_a[index], string_b[index])
        return build_result(index + 1, accumulated + next_char)

    return build_result(0, "")