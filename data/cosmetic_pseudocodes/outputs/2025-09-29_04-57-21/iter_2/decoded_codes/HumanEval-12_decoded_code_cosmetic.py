from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    longest_size: int = 0
    for item in list_of_strings:
        current_length = len(item)
        if current_length > longest_size:
            longest_size = current_length

    for element in list_of_strings:
        if len(element) == longest_size:
            return element