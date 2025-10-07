from collections import Counter
from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = Counter(lst)
    if any(count > 2 for count in count_digit.values()):
        return False
    return all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))