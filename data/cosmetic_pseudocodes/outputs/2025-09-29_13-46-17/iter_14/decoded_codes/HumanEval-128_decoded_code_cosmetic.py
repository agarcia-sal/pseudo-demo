from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None  # empty input yields None

    contains_zero = any(x == 0 for x in array_of_integers)
    if contains_zero:
        sign_product = 0
    else:
        # Collect all negative numbers
        negatives = {x for x in array_of_integers if x < 0}
        # sign_product is (-1) raised to count of negative numbers
        sign_product = (-1) ** len(negatives)

    # Sum of absolute values
    abs_sum = sum(abs(x) for x in array_of_integers)

    return sign_product * abs_sum