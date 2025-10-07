from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None
    if 0 in array_of_integers:
        product_sign_value = 0
    else:
        negatives_count = sum(1 for x in array_of_integers if x < 0)
        product_sign_value = (-1) ** negatives_count
    total_magnitude = sum(abs(number) for number in array_of_integers)
    return product_sign_value * total_magnitude