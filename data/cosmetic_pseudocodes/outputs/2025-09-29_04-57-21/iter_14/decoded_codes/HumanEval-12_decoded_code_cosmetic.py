from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    len_max: int = float('-inf')
    idx: int = 0
    while idx < len(list_of_strings):
        curr_len: int = len(list_of_strings[idx])
        if curr_len > len_max:
            len_max = curr_len
        idx += 1

    pos: int = 0
    while pos < len(list_of_strings):
        if not (len(list_of_strings[pos]) != len_max):
            return list_of_strings[pos]
        pos += 1

    # If no string found (theoretically unreachable), return None
    return None