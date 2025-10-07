from collections import Counter
from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = Counter(lst)
    for i in lst:
        if count_digit[i] > 2:
            return False
    for index in range(1, len(lst)):
        if lst[index - 1] > lst[index]:
            return False
    return True