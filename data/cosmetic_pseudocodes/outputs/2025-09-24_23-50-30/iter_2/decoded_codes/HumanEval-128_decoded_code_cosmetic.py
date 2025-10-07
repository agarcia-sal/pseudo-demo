from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    zero_found = False
    for i in range(len(array_of_integers)):
        if array_of_integers[i] == 0:
            zero_found = True
            break

    if zero_found:
        result_sign = 0
    else:
        negatives_count = 0
        for element in array_of_integers:
            if element < 0:
                negatives_count += 1
        result_sign = 1
        for _ in range(negatives_count):
            result_sign *= -1

    magnitudes_total = 0
    idx = len(array_of_integers) - 1
    while idx >= 0:
        magnitudes_total += array_of_integers[idx] * (-1 if array_of_integers[idx] < 0 else 1)
        idx -= 1

    return result_sign * magnitudes_total