from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None
    max_len: int = max((len(s) for s in list_of_strings), default=0)
    for element in list_of_strings:
        if len(element) == max_len:
            return element
    return None