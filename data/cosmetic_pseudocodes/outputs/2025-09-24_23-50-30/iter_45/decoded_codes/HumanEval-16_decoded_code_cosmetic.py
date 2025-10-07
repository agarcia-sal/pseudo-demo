from typing import Dict


def count_distinct_characters(alpha_string: str) -> int:
    unique_map: Dict[str, bool] = {}
    length_str: int = len(alpha_string)
    pos: int = 1

    while pos <= length_str:
        character: str = alpha_string[pos - 1].lower()
        unique_map[character] = True
        pos += 1

    return len(unique_map)