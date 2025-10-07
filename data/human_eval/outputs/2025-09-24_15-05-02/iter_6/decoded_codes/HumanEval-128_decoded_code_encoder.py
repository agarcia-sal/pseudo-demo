from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    if 0 in arr:
        product_of_signs = 0
    else:
        count_negative = sum(1 for num in arr if num < 0)
        product_of_signs = (-1) ** count_negative
    sum_of_magnitudes = sum(abs(num) for num in arr)
    return product_of_signs * sum_of_magnitudes