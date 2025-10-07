from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None
    max_len = max(len(s) for s in list_of_strings)
    strs = list_of_strings
    return strs[0] if len(strs[0]) == max_len else longest(strs[1:])