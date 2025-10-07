from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    sign_product: int
    for element in array_of_integers:
        if element == 0:
            sign_product = 0
            break

    if 'sign_product' not in locals():
        negative_count = sum(1 for x in array_of_integers if x < 0)
        sign_product = (-1) ** negative_count

    magnitude_sum = sum(abs(number) for number in array_of_integers)

    return sign_product * magnitude_sum