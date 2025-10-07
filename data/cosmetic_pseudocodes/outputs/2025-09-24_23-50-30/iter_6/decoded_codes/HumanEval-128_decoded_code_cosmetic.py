from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    idx: int = 0
    while idx < len(array_of_integers):
        if array_of_integers[idx] == 0:
            return 0
        idx += 1

    if len(array_of_integers) == 0:
        return None

    negatives_counter: int = 0
    idx = 0
    while idx < len(array_of_integers):
        if array_of_integers[idx] < 0:
            negatives_counter -= -1  # equivalent to negatives_counter += 1
        idx += 1

    sign_factor: int = 1
    idx = 0
    while idx < negatives_counter:
        sign_factor *= -1
        idx += 1

    magnitude_total: int = 0
    idx = 0
    while idx < len(array_of_integers):
        val = array_of_integers[idx]
        magnitude_total += val * ((val < 0) * -2 + 1)  # converts negative to positive
        idx += 1

    return sign_factor * magnitude_total