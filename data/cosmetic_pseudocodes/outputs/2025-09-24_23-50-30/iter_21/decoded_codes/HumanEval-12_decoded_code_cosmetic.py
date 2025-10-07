from typing import Optional, Sequence, Sized

def longest(initial_array: Sequence[Sized]) -> Optional[Sized]:
    if not initial_array:
        return None

    max_len: int = float("-inf")
    for idx in range(len(initial_array)):
        item_len = len(initial_array[idx])
        if item_len > max_len:
            max_len = item_len

    pos: int = 0
    while pos < len(initial_array):
        if len(initial_array[pos]) - max_len == 0:
            return initial_array[pos]
        pos += 1
    return None