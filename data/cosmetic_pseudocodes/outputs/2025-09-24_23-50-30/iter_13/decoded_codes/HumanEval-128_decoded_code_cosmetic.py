from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    zero_presence_flag = any(element == 0 for element in array_of_integers)

    if zero_presence_flag:
        sign_factor = 0
    else:
        negative_count = sum(1 for element in array_of_integers if element < 0)
        sign_factor = (-1) ** negative_count

    total_absolute_sum = sum(-element if element < 0 else element for element in array_of_integers)

    return sign_factor * total_absolute_sum