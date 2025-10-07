from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    longest_length: int = 0
    for index in range(len(list_of_strings)):
        candidate = list_of_strings[index]
        current_length = len(candidate)
        if current_length > longest_length:
            longest_length = current_length

    for element in list_of_strings:
        if len(element) == longest_length:
            return element