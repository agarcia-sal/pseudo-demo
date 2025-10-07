from typing import Set

def count_distinct_characters(str_param: str) -> int:
    temp_set: Set[str] = set()
    for char_elem in str_param:
        ch_lower = char_elem.lower()
        temp_set.add(ch_lower)
    return len(temp_set)