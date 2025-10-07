from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    zero_found: bool = False
    for num in array_of_integers:
        if num == 0:
            zero_found = True
            break

    if zero_found:
        sign_product = 0
    else:
        neg_counter: int = sum(1 for x in array_of_integers if x < 0)
        sign_product = 1 if (neg_counter % 2) == 0 else -1

    magnitude_sum: int = 0
    for num in array_of_integers:
        if num < 0:
            magnitude_sum -= num  # subtract negative = add abs(num)
        else:
            magnitude_sum += num

    return sign_product * magnitude_sum