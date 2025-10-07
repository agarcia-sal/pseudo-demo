from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None

    if 0 in arr:
        product_of_signs = 0
    else:
        count_negative = 0
        for element in arr:
            if element < 0:
                count_negative += 1
        product_of_signs = (-1) ** count_negative

    sum_of_magnitudes = 0
    for element in arr:
        sum_of_magnitudes += abs(element)

    return product_of_signs * sum_of_magnitudes