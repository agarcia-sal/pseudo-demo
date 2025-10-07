from typing import Iterator, Tuple

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        # Return '0' if characters are equal, else '1'
        return '0' if character_i == character_j else '1'

    output_accumulator = ""
    iterator_pairs = list(zip(string_a, string_b))  # convert to list to use len and indexing
    index_counter = 0
    while index_counter < len(iterator_pairs):
        left_char, right_char = iterator_pairs[index_counter]
        output_accumulator += xor(left_char, right_char)
        index_counter += 1

    return output_accumulator