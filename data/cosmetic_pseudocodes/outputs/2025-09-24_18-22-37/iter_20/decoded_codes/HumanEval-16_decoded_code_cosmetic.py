from typing import Set

def count_distinct_characters(str_param: str) -> int:
    idx_counter: int = 0
    char_lower: str = ''
    distinct_set: Set[str] = set()
    str_length: int = len(str_param)
    current_char: str = ''

    while idx_counter < str_length:
        current_char = str_param[idx_counter]
        char_lower = current_char.lower()
        distinct_set.add(char_lower)
        idx_counter += 1

    return len(distinct_set)