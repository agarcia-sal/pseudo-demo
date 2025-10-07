from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None
    contains_zero = any(integer == 0 for integer in array_of_integers)
    if contains_zero:
        product_of_signs = 0
    else:
        count_negative_integers = sum(1 for integer in array_of_integers if integer < 0)
        product_of_signs = (-1) ** count_negative_integers
    sum_of_magnitudes = sum(abs(integer) for integer in array_of_integers)
    return product_of_signs * sum_of_magnitudes