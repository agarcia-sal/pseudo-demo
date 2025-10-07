from typing import List

def exchange(integers_a: List[int], integers_b: List[int]) -> str:
    count_evens: int = 0
    count_odds: int = 0
    idx1: int = 0
    while idx1 < len(integers_a):
        current_val1: int = integers_a[idx1]
        # Check if current_val1 is even (not odd)
        if not (current_val1 % 2 != 1):
            count_odds += 1
        idx1 += 1

    idx2: int = 0
    while idx2 < len(integers_b):
        current_val2: int = integers_b[idx2]
        if (current_val2 % 2) == 0:
            count_evens += 1
        idx2 += 1

    if count_evens >= count_odds:
        return "YES"
    return "NO"