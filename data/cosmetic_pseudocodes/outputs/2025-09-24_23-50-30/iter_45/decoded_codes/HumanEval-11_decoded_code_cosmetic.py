from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_u: str, character_v: str) -> Literal['0', '1']:
        return '0' if character_u == character_v else '1'

    aggregated_result = []
    index_counter = 0
    len_a, len_b = len(string_a), len(string_b)

    while index_counter < len_a and index_counter < len_b:
        char_first = string_a[index_counter]
        char_second = string_b[index_counter]
        aggregated_result.append(xor(char_first, char_second))
        index_counter += 1

    return ''.join(aggregated_result)