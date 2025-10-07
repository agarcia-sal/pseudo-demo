from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len: int = -1
    idx: int = 0

    while idx < len(list_of_strings):
        current_str = list_of_strings[idx]
        if len(current_str) > max_len:
            max_len = len(current_str)
        idx += 1

    pointer: int = 0
    while pointer < len(list_of_strings):
        candidate = list_of_strings[pointer]
        if len(candidate) == max_len:
            return candidate
        pointer += 1

    return None