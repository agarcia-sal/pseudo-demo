from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    result_string: str = ""
    index: int = 0
    while index < len(string_a) and index < len(string_b):
        result_string += xor(string_a[index], string_b[index])
        index += 1
    return result_string