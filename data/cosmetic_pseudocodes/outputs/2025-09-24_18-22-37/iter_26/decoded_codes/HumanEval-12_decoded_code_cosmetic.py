from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    count: int = len(list_of_strings)
    if count == 0:
        return None

    max_len: int = -1
    idx: int = 0
    while idx < count:
        temp_len: int = len(list_of_strings[idx])
        if temp_len > max_len:
            max_len = temp_len
        idx += 1

    idx = 0
    while idx < count:
        candidate: str = list_of_strings[idx]
        temp_len = len(candidate)
        if temp_len == max_len:
            return candidate
        idx += 1