from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len: int = float('-inf')
    idx: int = 0
    while idx < len(list_of_strings):
        current_length = len(list_of_strings[idx])
        if current_length > max_len:
            max_len = current_length
        idx += 1

    pos: int = 0
    while pos < len(list_of_strings):
        candidate = list_of_strings[pos]
        if len(candidate) == max_len:
            return candidate
        pos += 1
    # Implicitly returns None if something unexpected happens (e.g., empty input handled above)