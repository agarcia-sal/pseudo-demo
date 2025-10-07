from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    contains_zero = False
    negative_count = 0
    for index in range(len(arr)):
        if arr[index] == 0:
            contains_zero = True
        if arr[index] < 0:
            negative_count += 1
    if contains_zero:
        prod = 0
    else:
        power = negative_count
        prod = 1
        for count in range(1, power + 1):
            prod *= -1
    total_sum = 0
    for index in range(len(arr)):
        if arr[index] >= 0:
            abs_value = arr[index]
        else:
            abs_value = arr[index] * -1
        total_sum += abs_value
    return prod * total_sum