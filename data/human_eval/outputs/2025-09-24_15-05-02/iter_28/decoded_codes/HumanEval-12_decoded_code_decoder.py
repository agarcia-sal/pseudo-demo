from typing import Optional, List

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None
    max_length = max(len(s) for s in list_of_strings)
    for s in list_of_strings:
        if len(s) == max_length:
            return s