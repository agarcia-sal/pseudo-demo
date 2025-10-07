from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    for each_elem in array_of_integers:
        if each_elem == 0:
            result_sign = 0
            break
    else:
        negative_count = sum(1 for x in array_of_integers if x < 0)
        result_sign = 1 - 2 * (negative_count % 2)

    total_magnitude = sum(abs(value) for value in array_of_integers)
    return result_sign * total_magnitude