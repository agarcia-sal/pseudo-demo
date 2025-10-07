from typing import Set


def count_distinct_characters(str_param: str) -> int:
    char_set: Set[str] = set()
    length_val: int = len(str_param)
    idx: int = 0
    while idx < length_val:
        lower_char: str = str_param[idx].lower()
        if lower_char not in char_set:
            char_set.add(lower_char)
        idx += 1
    return len(char_set)