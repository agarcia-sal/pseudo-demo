from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len: int = float("-inf")
    index: int = 0
    while index < len(list_of_strings):
        current_str = list_of_strings[index]
        current_length = len(current_str)
        if current_length > max_len:
            max_len = current_length
        index += 1

    position: int = 0
    while position < len(list_of_strings):
        candidate = list_of_strings[position]
        if len(candidate) == max_len:
            return candidate
        position += 1