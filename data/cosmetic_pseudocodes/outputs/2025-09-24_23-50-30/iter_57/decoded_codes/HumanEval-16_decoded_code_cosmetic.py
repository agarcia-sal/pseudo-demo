from typing import Set

def count_distinct_characters(str_param: str) -> int:
    unique_chars: Set[str] = set()
    idx: int = 0
    while idx < len(str_param):
        current_char = str_param[idx].lower()
        if current_char not in unique_chars:
            unique_chars.add(current_char)
        idx += 1
    return len(unique_chars)