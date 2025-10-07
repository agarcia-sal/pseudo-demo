from typing import Optional, List


def prod_sign(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    has_zero: bool = False
    idx: int = 0
    length = len(array_of_integers)

    while idx < length:
        if array_of_integers[idx] == 0:
            has_zero = True
            break
        idx += 1

    if has_zero:
        product_sign = 0
    else:
        negative_counter = 0
        idx = 0
        while idx < length:
            if array_of_integers[idx] < 0:
                negative_counter += 1
            idx += 1
        product_sign = (-1) ** negative_counter

    total_absolute_sum = 0
    index_ptr = 0
    while index_ptr < length:
        total_absolute_sum += abs(array_of_integers[index_ptr])
        index_ptr += 1

    return product_sign * total_absolute_sum