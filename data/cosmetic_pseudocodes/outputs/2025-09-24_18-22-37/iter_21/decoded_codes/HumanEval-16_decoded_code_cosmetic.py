from typing import Set


def count_distinct_characters(str_param: str) -> int:
    char_set: Set[str] = set()
    idx: int = 0
    while idx < len(str_param):
        curr_char: str = str_param[idx].lower()
        if curr_char not in char_set:
            char_set.add(curr_char)
        idx += 1
    return len(char_set)