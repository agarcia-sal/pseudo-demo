from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    result_list: List[str] = []
    index: int = 0
    length_a: int = len(string_a)
    length_b: int = len(string_b)
    while index < length_a and index < length_b:
        ch1 = string_a[index]
        ch2 = string_b[index]
        result_list.append(xor(ch1, ch2))
        index += 1
    return ''.join(result_list)