from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = {}
    for i in range(len(lst)):
        count_digit[lst[i]] = 0
    for j in range(len(lst)):
        count_digit[lst[j]] += 1
    for k in range(len(lst)):
        if count_digit[lst[k]] > 2:
            return False
    for m in range(1, len(lst)):
        if lst[m - 1] > lst[m]:
            return False
    return True