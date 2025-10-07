from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if 0 in array_of_integers:
        interim_sign = 0
    else:
        negatives_filtered_length = sum(1 for each_element in array_of_integers if each_element < 0)
        interim_sign = (-1) ** negatives_filtered_length

    aggregate_magnitude = sum(abs(x) for x in array_of_integers)

    return interim_sign * aggregate_magnitude