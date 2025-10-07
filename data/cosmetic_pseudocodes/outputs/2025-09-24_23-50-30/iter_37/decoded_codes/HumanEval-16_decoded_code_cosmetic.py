from typing import List, Set


def count_distinct_characters(str_param: str) -> int:
    chars_list: List[str] = []
    idx: int = 0
    lowered: str = ""
    while idx < len(str_param):
        lowered += str_param[idx].lower()
        idx += 1
    distinct_chars: Set[str] = set()
    l_idx: int = 0
    while l_idx < len(lowered):
        current_char: str = lowered[l_idx]
        if current_char not in distinct_chars:
            distinct_chars.add(current_char)
        l_idx += 1
    return len(distinct_chars)