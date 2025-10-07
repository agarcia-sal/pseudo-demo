from typing import Dict

def count_distinct_characters(text_input: str) -> int:
    character_map: Dict[str, bool] = {}
    position_index: int = 0
    length_text: int = len(text_input)
    while position_index < length_text:
        current_char: str = text_input[position_index].lower()
        character_map[current_char] = True
        position_index += 1
    distinct_count: int = 0
    for key_char in character_map.keys():
        distinct_count += 1
    return distinct_count