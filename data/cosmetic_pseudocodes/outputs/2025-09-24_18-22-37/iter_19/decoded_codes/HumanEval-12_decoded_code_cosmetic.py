from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len: int = 0
    idx: int = 0

    while idx < len(list_of_strings):
        str_elem = list_of_strings[idx]
        candidate = len(str_elem)
        if candidate > max_len:
            max_len = candidate
        idx += 1

    idx = 0
    while idx < len(list_of_strings):
        str_elem = list_of_strings[idx]
        if not (len(str_elem) != max_len):
            return str_elem
        idx += 1
    return None