from typing import List, Optional


def prod_sign(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if 0 in array_of_integers:
        product_sign = 0
    else:
        negative_count = sum(1 for x in array_of_integers if x < 0)
        product_sign = (-1) ** negative_count

    magnitude_sum = sum(abs(number) for number in array_of_integers)

    return product_sign * magnitude_sum