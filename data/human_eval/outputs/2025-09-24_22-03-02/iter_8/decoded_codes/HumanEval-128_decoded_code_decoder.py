from typing import List, Optional

def prod_sign(arr: List[int]) -> Optional[int]:
    if not arr:
        return None

    contains_zero = False
    for item in arr:
        if item == 0:
            contains_zero = True
            break

    if contains_zero:
        product_sign = 0
    else:
        negative_count = 0
        for item in arr:
            if item < 0:
                negative_count += 1
        if negative_count % 2 == 0:
            product_sign = 1
        else:
            product_sign = -1

    sum_magnitudes = 0
    for item in arr:
        sum_magnitudes += abs(item)

    return product_sign * sum_magnitudes