from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    contains_zero = 0 in arr
    if contains_zero:
        product_of_signs = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        product_of_signs = (-1) ** negative_count
    sum_of_magnitudes = sum(abs(x) for x in arr)
    return product_of_signs * sum_of_magnitudes