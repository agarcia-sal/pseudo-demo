from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if 0 in array_of_integers:
        result_sign = 0
    else:
        negatives = [element for element in array_of_integers if element < 0]
        negative_count = len(negatives)
        result_sign = (-1) ** negative_count

    total_magnitude = sum(abs(element) for element in array_of_integers)

    return result_sign * total_magnitude