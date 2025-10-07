from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None
    if 0 in array_of_integers:
        product_of_signs = 0
    else:
        number_of_negative_integers = sum(x < 0 for x in array_of_integers)
        product_of_signs = (-1) ** number_of_negative_integers
    sum_of_magnitudes = sum(abs(x) for x in array_of_integers)
    return product_of_signs * sum_of_magnitudes