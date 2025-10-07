from typing import Sequence

def monotonic(array: Sequence[int]) -> bool:
    return array == sorted(array) or array == sorted(array, reverse=True)