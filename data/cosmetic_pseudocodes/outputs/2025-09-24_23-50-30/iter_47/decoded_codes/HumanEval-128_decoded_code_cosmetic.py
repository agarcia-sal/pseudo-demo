from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    for num in array_of_integers:
        if num == 0:
            return 0

    neg_count = sum(1 for num in array_of_integers if num < 0)

    base_product = (-1) ** neg_count

    total_abs_sum = sum(abs(num) for num in array_of_integers)

    return base_product * total_abs_sum