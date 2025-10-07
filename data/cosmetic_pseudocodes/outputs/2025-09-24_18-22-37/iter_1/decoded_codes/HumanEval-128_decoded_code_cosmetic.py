from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if 0 in array_of_integers:
        sign_product = 0
    else:
        negative_count = sum(1 for number in array_of_integers if number < 0)
        sign_product = (-1) ** negative_count

    magnitude_sum = sum(abs(num) for num in array_of_integers)

    return sign_product * magnitude_sum