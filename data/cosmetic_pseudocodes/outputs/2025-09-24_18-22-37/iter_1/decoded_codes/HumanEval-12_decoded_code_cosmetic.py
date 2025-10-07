from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len = 0
    for string in list_of_strings:
        if len(string) > max_len:
            max_len = len(string)

    for string in list_of_strings:
        if len(string) == max_len:
            return string