from typing import List, Optional

def prod_signs(array: List[int]) -> Optional[int]:
    if not array:
        return None
    if 0 in array:
        product_of_signs = 0
    else:
        count_negative = sum(1 for x in array if x < 0)
        product_of_signs = (-1) ** count_negative
    sum_of_magnitudes = sum(abs(x) for x in array)
    return product_of_signs * sum_of_magnitudes