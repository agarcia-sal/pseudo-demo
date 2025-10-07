from typing import Sequence, Optional

def prod_signs(sequence_of_ints: Sequence[int]) -> Optional[int]:
    if len(sequence_of_ints) == 0:
        return None

    zero_found = False
    neg_count = 0

    idx = 0
    while idx < len(sequence_of_ints):
        current_val = sequence_of_ints[idx]
        if current_val == 0:
            zero_found = True
            break
        if current_val < 0:
            neg_count += 1
        idx += 1

    if zero_found:
        product_sign = 0
    else:
        exponentiation_base = -1
        exponentiation_result = 1
        exponent_itr = 0
        while exponent_itr < neg_count:
            exponentiation_result *= exponentiation_base
            exponent_itr += 1
        product_sign = exponentiation_result

    total_magnitude = 0
    for element in sequence_of_ints:
        abs_val = element if element >= 0 else -element  # manual abs
        total_magnitude += abs_val

    return product_sign * total_magnitude