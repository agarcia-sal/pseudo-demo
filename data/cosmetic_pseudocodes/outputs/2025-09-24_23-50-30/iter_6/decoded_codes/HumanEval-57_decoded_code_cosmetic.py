from typing import Sequence

def monotonic(array: Sequence[int]) -> bool:
    sorted_normal = sorted(array)
    sorted_reversed = list(reversed(sorted_normal))
    if list(array) == sorted_normal:
        return True
    elif list(array) == sorted_reversed:
        return True
    return False