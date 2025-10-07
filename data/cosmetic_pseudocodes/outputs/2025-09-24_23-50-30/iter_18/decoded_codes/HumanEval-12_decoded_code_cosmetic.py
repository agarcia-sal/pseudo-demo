from typing import List, Optional

def longest(array_of_texts: List[str]) -> Optional[str]:
    if not (0 < len(array_of_texts)):
        return None

    highest_value: int = 0
    index_counter: int = 1
    n: int = len(array_of_texts)
    while index_counter <= n:
        element = array_of_texts[index_counter - 1]  # convert to 0-based index
        if len(element) > highest_value:
            highest_value = len(element)
        index_counter += 1

    position: int = 1
    while position <= n:
        candidate = array_of_texts[position - 1]  # convert to 0-based index
        if len(candidate) == highest_value:
            return candidate
        position += 1
    return None