from typing import Optional, Sequence


def prod_sign(array_of_integers: Sequence[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    contains_zero_flag: bool = False
    for element in array_of_integers:
        if element == 0:
            contains_zero_flag = True
            break

    if contains_zero_flag:
        result_sign = 0
    else:
        negative_quantity = sum(1 for value in array_of_integers if value < 0)
        result_sign = 1 if (negative_quantity % 2) == 0 else -1

    total_magnitude = 0
    for val in array_of_integers:
        if val < 0:
            total_magnitude -= val  # subtract negative to add its absolute value
        else:
            total_magnitude += val

    return result_sign * total_magnitude