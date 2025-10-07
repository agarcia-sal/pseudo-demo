from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    maximum_length: int = max(len(s) for s in list_of_strings)

    for s in list_of_strings:
        if len(s) == maximum_length:
            return s