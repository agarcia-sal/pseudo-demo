from typing import List


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        if character_i == character_j:
            return '0'
        return '1'

    accumulator: List[str] = []
    index_m: int = 0
    limit_n: int = len(string_a)

    while index_m < limit_n:
        current_pair = (string_a[index_m], string_b[index_m])
        accumulator.append(xor(current_pair[0], current_pair[1]))
        index_m += 1

    return ''.join(accumulator)