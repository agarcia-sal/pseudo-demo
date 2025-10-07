from typing import List, Optional


def prod_sign(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    zero_found = any(element == 0 for element in array_of_integers)
    if zero_found:
        product_sign = 0
    else:
        negative_count = sum(1 for value in array_of_integers if value < 0)
        product_sign = -1 if negative_count % 2 == 1 else 1

    total_magnitude = sum(abs(num) for num in array_of_integers)

    return product_sign * total_magnitude