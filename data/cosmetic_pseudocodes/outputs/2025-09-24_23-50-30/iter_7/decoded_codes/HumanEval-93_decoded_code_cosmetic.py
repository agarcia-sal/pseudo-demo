from typing import Dict, List

def encode(input_text: str) -> str:
    vowels_collection: str = "aeiouAEIOU"
    mapping_table: Dict[str, str] = {}

    for character in vowels_collection:
        mapping_table[character] = chr(ord(character) + 2)

    swapped_text: str = ''.join(
        ch.upper() if ch.islower() else ch.lower() if ch.isupper() else ch
        for ch in input_text
    )

    def transform_position(position: int, text_seq: str, map_ref: Dict[str, str], collected: List[str]) -> None:
        if position == len(text_seq):
            return
        current_character = text_seq[position]
        if current_character in vowels_collection:
            collected.append(map_ref[current_character])
        else:
            collected.append(current_character)
        transform_position(position + 1, text_seq, map_ref, collected)

    result_builder: List[str] = []
    transform_position(0, swapped_text, mapping_table, result_builder)
    return ''.join(result_builder)