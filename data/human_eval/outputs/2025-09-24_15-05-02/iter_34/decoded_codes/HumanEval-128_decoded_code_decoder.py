from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None
    if 0 in array_of_integers:
        sign_product = 0
    else:
        count_of_negative_numbers = sum(1 for x in array_of_integers if x < 0)
        sign_product = (-1) ** count_of_negative_numbers
    sum_of_magnitudes = sum(abs(x) for x in array_of_integers)
    return sign_product * sum_of_magnitudes