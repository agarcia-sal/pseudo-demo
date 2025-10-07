from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    maximum_length = max(len(s) for s in list_of_strings)

    for string in list_of_strings:
        if len(string) == maximum_length:
            return string