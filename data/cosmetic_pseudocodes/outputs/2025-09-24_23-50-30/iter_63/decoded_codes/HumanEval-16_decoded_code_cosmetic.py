from typing import Set

def count_distinct_characters(input_string: str) -> int:
    temp_set: Set[str] = set()
    idx: int = 0

    while idx < len(input_string):
        current_char: str = input_string[idx].lower()
        temp_set |= {current_char}
        idx += 1

    return len(temp_set)