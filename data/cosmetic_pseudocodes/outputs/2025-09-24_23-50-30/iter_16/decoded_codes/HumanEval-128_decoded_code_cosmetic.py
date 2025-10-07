from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if 0 in array_of_integers:
        product_sign = 0
    else:
        neg_count = sum(1 for value in array_of_integers if value < 0)
        product_sign = 1 + (-2) * (neg_count % 2)

    magnitude_sum = sum(-element if element < 0 else element for element in array_of_integers)
    return product_sign * magnitude_sum