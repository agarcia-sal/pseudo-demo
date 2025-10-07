from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if 0 in array_of_integers:
        product_of_signs: int = 0
    else:
        count_negative_numbers: int = sum(1 for num in array_of_integers if num < 0)
        product_of_signs = (-1) ** count_negative_numbers

    sum_of_magnitudes: int = sum(abs(num) for num in array_of_integers)

    return product_of_signs * sum_of_magnitudes