from typing import Optional, Sequence

def longest(collection: Sequence[str]) -> Optional[str]:
    index: int = 0
    max_len: int = -1
    selected: Optional[str] = None

    while index < len(collection):
        current_string = collection[index]
        current_length = len(current_string)
        if max_len < current_length:
            selected = current_string
            max_len = current_length
        index += 1

    return selected