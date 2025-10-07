from collections import Counter
from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = Counter(lst)
    if any(v > 2 for v in count_digit.values()):
        return False
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True