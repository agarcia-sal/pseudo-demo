from typing import List


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        # Return '0' if characters are equal, else '1'
        return '0' if character_i == character_j else '1'

    def fold_xor(accumulator: str, pair_list: List[List[str]], index: int) -> str:
        if index >= len(pair_list):
            return accumulator
        pair = pair_list[index]
        bit = xor(pair[0], pair[1])
        return fold_xor(accumulator + bit, pair_list, index + 1)

    pairs: List[List[str]] = []
    limit = min(len(string_a), len(string_b))
    for i in range(limit):
        pairs.append([string_a[i], string_b[i]])

    return fold_xor("", pairs, 0)