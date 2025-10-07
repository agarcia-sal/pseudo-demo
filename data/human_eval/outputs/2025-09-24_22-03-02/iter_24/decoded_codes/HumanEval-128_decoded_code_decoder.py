from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if arr == []:
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
        prod = 1
        exponent = negative_count
        while exponent > 0:
            prod *= -1
            exponent -= 1

    sum_magnitude = 0
    for index in range(len(arr)):
        if arr[index] >= 0:
            magnitude = arr[index]
        else:
            magnitude = 0 - arr[index]
        sum_magnitude += magnitude

    return prod * sum_magnitude