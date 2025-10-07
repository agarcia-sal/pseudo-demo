from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        if character_i == character_j:
            return '0'
        else:
            return '1'

    aggregate_list: List[str] = []
    index_counter: int = 0

    while index_counter < len(string_a) and index_counter < len(string_b):
        aggregate_list.append(xor(string_a[index_counter], string_b[index_counter]))
        index_counter += 1

    accumulated_string: str = ''.join(aggregate_list)
    return accumulated_string