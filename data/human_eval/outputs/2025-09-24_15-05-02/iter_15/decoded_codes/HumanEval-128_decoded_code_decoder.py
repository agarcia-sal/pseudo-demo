from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    if 0 in arr:
        product_of_signs = 0
    else:
        negative_count = sum(1 for element in arr if element < 0)
        product_of_signs = (-1) ** negative_count
    sum_of_magnitudes = sum(abs(element) for element in arr)
    return product_of_signs * sum_of_magnitudes