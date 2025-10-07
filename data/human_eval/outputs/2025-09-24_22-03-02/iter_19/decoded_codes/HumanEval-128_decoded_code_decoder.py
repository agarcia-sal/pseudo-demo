from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    contains_zero = False
    negative_count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            contains_zero = True
        if arr[i] < 0:
            negative_count += 1
    if contains_zero:
        prod = 0
    else:
        prod = 1
        for _ in range(negative_count):
            prod *= -1
    total_abs_sum = 0
    for i in range(len(arr)):
        total_abs_sum += abs(arr[i])
    return prod * total_abs_sum