from typing import List, Tuple


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        if character_i == character_j:
            return '0'
        return '1'

    accumulated_result: List[str] = []

    def process_pairs(pair_list: List[Tuple[str, str]], index: int) -> None:
        if index == len(pair_list):
            return
        first_char, second_char = pair_list[index]
        accumulated_result.append(xor(first_char, second_char))
        process_pairs(pair_list, index + 1)

    zipped_characters: List[Tuple[str, str]] = list(zip(string_a, string_b))
    process_pairs(zipped_characters, 0)

    return ''.join(accumulated_result)