from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len: int = 0
    index_counter: int = 0

    while index_counter < len(list_of_strings):
        current_item = list_of_strings[index_counter]
        if len(current_item) > max_len:
            max_len = len(current_item)
        index_counter += 1

    pointer: int = 0
    while pointer < len(list_of_strings):
        element = list_of_strings[pointer]
        if len(element) == max_len:
            return element
        pointer += 1