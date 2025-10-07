from typing import List, Optional

def prod_signs(list_of_integers: List[int]) -> Optional[int]:
    if not list_of_integers:
        return None

    if 0 in list_of_integers:
        product_of_signs = 0
    else:
        count_of_negatives = sum(1 for integer in list_of_integers if integer < 0)
        product_of_signs = (-1) ** count_of_negatives

    sum_of_magnitudes = sum(abs(integer) for integer in list_of_integers)

    return product_of_signs * sum_of_magnitudes