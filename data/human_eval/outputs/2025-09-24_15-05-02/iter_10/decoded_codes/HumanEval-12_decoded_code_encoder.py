from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if len(list_of_strings) == 0:
        return None
    max_length = 0
    for string in list_of_strings:
        if len(string) > max_length:
            max_length = len(string)
    for string in list_of_strings:
        if len(string) == max_length:
            return string