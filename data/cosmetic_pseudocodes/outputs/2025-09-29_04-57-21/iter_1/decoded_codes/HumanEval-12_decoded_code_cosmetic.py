from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len = 0
    for item in list_of_strings:
        if len(item) > max_len:
            max_len = len(item)

    for element in list_of_strings:
        if len(element) == max_len:
            return element