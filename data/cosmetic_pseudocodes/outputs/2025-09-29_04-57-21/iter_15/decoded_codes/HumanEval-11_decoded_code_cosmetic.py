from typing import Iterator

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        # Return '0' if characters are equal, '1' otherwise
        return '0' if character_p == character_q else '1'

    accumulated_result = ""
    iterator_pairs = list(zip(string_b, string_a))  # materialize to index
    current_index = 0

    while current_index < len(iterator_pairs):
        pair_item = iterator_pairs[current_index]
        first_char = pair_item[1]
        second_char = pair_item[0]
        accumulated_result += xor(second_char, first_char)
        current_index += 1

    return accumulated_result