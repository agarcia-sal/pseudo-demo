from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    prod = 0
    for index in range(len(arr)):
        if arr[index] == 0:
            prod = 0
            break
    if prod != 0:
        negative_count = 0
        for index in range(len(arr)):
            if arr[index] < 0:
                negative_count += 1
        prod = 1
        while negative_count > 0:
            prod *= -1
            negative_count -= 1
    sum_abs = 0
    for index in range(len(arr)):
        sum_abs += abs(arr[index])
    return prod * sum_abs