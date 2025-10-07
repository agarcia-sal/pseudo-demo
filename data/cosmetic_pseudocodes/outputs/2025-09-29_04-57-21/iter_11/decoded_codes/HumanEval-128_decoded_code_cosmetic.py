from typing import List, Optional


def prod_signs(array_of_integers: Optional[List[int]]) -> Optional[int]:
    if not array_of_integers:
        return None

    if any(element == 0 for element in array_of_integers):
        sign_accumulator = 0
    else:
        negative_count = sum(1 for element in array_of_integers if element < 0)
        sign_accumulator = (-1) ** negative_count

    magnitude_total = 0
    for element in array_of_integers:
        # multiply by +1 if element >= 0, else -1 if element < 0
        magnitude_total += element * ((element >= 0) - (element < 0))

    return sign_accumulator * magnitude_total