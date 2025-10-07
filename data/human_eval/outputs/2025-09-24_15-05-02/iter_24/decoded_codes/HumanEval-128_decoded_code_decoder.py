from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if 0 in array_of_integers:
        product_of_signs = 0
    else:
        count_of_negative_numbers = sum(1 for element in array_of_integers if element < 0)
        product_of_signs = (-1) ** count_of_negative_numbers

    sum_of_magnitudes = sum(abs(element) for element in array_of_integers)
    return product_of_signs * sum_of_magnitudes