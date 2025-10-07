from typing import List, Optional


def prod_sign(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    if 0 in array_of_integers:
        result_sign = 0
    else:
        negative_count = 0
        index = 0
        while index < len(array_of_integers):
            if array_of_integers[index] < 0:
                negative_count += 1
            index += 1
        result_sign = (-1) ** negative_count

    total_magnitude = sum(abs(element) for element in array_of_integers)

    return result_sign * total_magnitude