from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = {i: 0 for i in lst}
    for i in lst:
        count_digit[i] += 1
    for i in lst:
        if count_digit[i] > 2:
            return False
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True