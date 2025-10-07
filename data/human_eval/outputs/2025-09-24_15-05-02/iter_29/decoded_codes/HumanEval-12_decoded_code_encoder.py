from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None
    max_len = max(len(s) for s in list_of_strings)
    for s in list_of_strings:
        if len(s) == max_len:
            return s