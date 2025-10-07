from typing import Dict


def count_distinct_characters(source_text: str) -> int:
    char_map: Dict[str, bool] = {}
    iterator_index: int = 0

    while iterator_index < len(source_text):
        current_char: str = source_text[iterator_index].lower()
        char_map[current_char] = True
        iterator_index += 1

    return len(char_map)