from typing import List, Tuple

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_m: str, character_n: str) -> str:
        if character_m == character_n:
            return '0'
        else:
            return '1'

    def traverse_pairs(pairs_list: List[Tuple[str, str]], accumulator: str) -> str:
        if not pairs_list:
            return accumulator
        first_char1, first_char2 = pairs_list[0]
        updated_accumulator = accumulator + xor(first_char1, first_char2)
        return traverse_pairs(pairs_list[1:], updated_accumulator)

    zipped_pairs = list(zip(string_a, string_b))
    return traverse_pairs(zipped_pairs, "")