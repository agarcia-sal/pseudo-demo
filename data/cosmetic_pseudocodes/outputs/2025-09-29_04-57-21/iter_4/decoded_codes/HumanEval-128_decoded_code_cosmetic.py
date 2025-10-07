from typing import List, Optional


def prod_sign(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    zero_found = False
    position = 0
    length = len(array_of_integers)

    while not zero_found and position < length:
        if array_of_integers[position] == 0:
            zero_found = True
        else:
            position += 1

    if zero_found:
        product_sign = 0
    else:
        negatives_qty = 0
        idx = 0
        while idx < length:
            if array_of_integers[idx] < 0:
                negatives_qty += 1
            idx += 1
        product_sign = 1
        for _ in range(negatives_qty):
            product_sign *= -1

    total_magnitude = 0
    i = 0
    while i < length:
        if array_of_integers[i] < 0:
            total_magnitude -= array_of_integers[i]
        else:
            total_magnitude += array_of_integers[i]
        i += 1

    return product_sign * total_magnitude