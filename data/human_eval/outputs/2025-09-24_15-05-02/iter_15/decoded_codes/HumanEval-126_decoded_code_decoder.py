from typing import List
from collections import Counter

def is_sorted(lst: List[int]) -> bool:
    count_digit = Counter()
    for element in lst:
        count_digit[element] += 1
    if any(count_digit[element] > 2 for element in lst):
        return False
    return all(lst[i-1] <= lst[i] for i in range(1, len(lst)))