from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if any(element == 0 for element in array_of_integers):
        sign_product = 0
    else:
        negatives_count = sum(1 for num in array_of_integers if num < 0)
        sign_product = (-1) ** negatives_count

    total_magnitude = sum(abs(value) for value in array_of_integers)

    return sign_product * total_magnitude