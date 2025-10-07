from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    length: int = len(string_a)
    chars_list: List[str] = []

    for idx in range(length):
        chars_list.append(xor(string_a[idx], string_b[idx]))

    return ''.join(chars_list)