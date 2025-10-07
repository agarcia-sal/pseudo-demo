from typing import List

def maximum(array_of_integers: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    sorted_array = sorted(array_of_integers)
    return sorted_array[-k:] if k <= len(sorted_array) else sorted_array[:]