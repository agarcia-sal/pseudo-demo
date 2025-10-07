from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None

    contains_zero = False
    negative_count = 0

    for element in arr:
        if element == 0:
            contains_zero = True
        elif element < 0:
            negative_count += 1

    if contains_zero:
        product_sign = 0
    else:
        product_sign = (-1) ** negative_count

    sum_magnitudes = sum(abs(element) for element in arr)

    return product_sign * sum_magnitudes