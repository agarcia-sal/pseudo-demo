from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    contains_zero = False
    negative_count = 0
    for x in arr:
        if x == 0:
            contains_zero = True
        elif x < 0:
            negative_count += 1
    if contains_zero:
        prod = 0
    else:
        prod = (-1) ** negative_count
    sum_of_magnitudes = sum(abs(x) for x in arr)
    return prod * sum_of_magnitudes