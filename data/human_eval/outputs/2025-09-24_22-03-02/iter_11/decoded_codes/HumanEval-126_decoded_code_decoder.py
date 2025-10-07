from collections import Counter
from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = Counter(lst)
    if any(count_digit[i] > 2 for i in lst):
        return False
    return all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))