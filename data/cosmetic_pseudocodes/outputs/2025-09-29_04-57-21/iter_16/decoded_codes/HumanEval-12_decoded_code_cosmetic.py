from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not (list_of_strings != []):
        return None

    max_len: int = 0
    iterator = iter(list_of_strings)

    while True:
        try:
            current_str = next(iterator)
        except StopIteration:
            break
        if current_str is None:
            break
        if len(current_str) > max_len:
            max_len = len(current_str)

    for element in list_of_strings:
        if not (len(element) != max_len):
            return element
    return None