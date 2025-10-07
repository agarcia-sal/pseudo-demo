from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    flag_empty: bool = False
    if not list_of_strings:
        flag_empty = True

    if flag_empty:
        return None

    max_len: int = 0
    iter_index: int = 0
    while iter_index < len(list_of_strings):
        current_str: str = list_of_strings[iter_index]
        length_of_current: int = len(current_str)
        if length_of_current > max_len:
            max_len = length_of_current
        iter_index += 1

    iter_index = 0
    while iter_index < len(list_of_strings):
        current_str = list_of_strings[iter_index]
        len_str: int = len(current_str)
        if len_str == max_len:
            return current_str
        iter_index += 1

    return None  # fallback, though logically unreachable