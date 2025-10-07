from typing import List


def sort_array(k1: List[int]) -> List[int]:
    # Check if the list is empty
    if len(k1) == 0:
        return []
    # Determine if sum of first and last elements is even
    k4: int = k1[0] + k1[-1]
    k5: bool = (k4 % 2 == 0)
    # Sort ascending if k5 is True, else descending
    return sorted(k1, reverse=not k5)