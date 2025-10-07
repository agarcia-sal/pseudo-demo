from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings or len(list_of_strings) == 0:
        return None

    maxLen: int = -1
    idx: int = 0

    while idx < len(list_of_strings):
        if len(list_of_strings[idx]) > maxLen:
            maxLen = len(list_of_strings[idx])
        idx += 1

    idx = 0
    while idx < len(list_of_strings):
        if len(list_of_strings[idx]) == maxLen:
            return list_of_strings[idx]
        idx += 1