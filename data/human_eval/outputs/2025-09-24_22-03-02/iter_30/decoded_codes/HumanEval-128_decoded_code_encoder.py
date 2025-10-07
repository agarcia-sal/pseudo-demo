from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    contains_zero = False
    count_negative = 0
    index = 0
    while index < len(arr):
        if arr[index] == 0:
            contains_zero = True
        if arr[index] < 0:
            count_negative += 1
        index += 1
    if contains_zero:
        prod = 0
    else:
        exponent = count_negative
        prod = 1
        while exponent > 0:
            prod *= -1
            exponent -= 1
    total_sum = 0
    index = 0
    while index < len(arr):
        if arr[index] < 0:
            absolute_value = arr[index] * -1
        else:
            absolute_value = arr[index]
        total_sum += absolute_value
        index += 1
    result = prod * total_sum
    return result