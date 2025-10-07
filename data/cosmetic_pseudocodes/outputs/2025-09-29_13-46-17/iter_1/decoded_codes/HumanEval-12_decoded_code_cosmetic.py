from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if list_of_strings:
        max_len: int = 0
        for string in list_of_strings:
            if len(string) > max_len:
                max_len = len(string)
        for string in list_of_strings:
            if len(string) == max_len:
                return string
    else:
        return None