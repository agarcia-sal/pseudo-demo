from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    zero_exists = False
    for element in arr:
        if element == 0:
            zero_exists = True
            break
    if zero_exists:
        prod = 0
    else:
        negative_count = 0
        for element in arr:
            if element < 0:
                negative_count += 1
        length = 0
        for _ in arr:
            length += 1
        prod = (-1) ** negative_count
    sum_magnitudes = 0
    for element in arr:
        if element >= 0:
            magnitude = element
        else:
            magnitude = -element
        sum_magnitudes += magnitude
    return prod * sum_magnitudes