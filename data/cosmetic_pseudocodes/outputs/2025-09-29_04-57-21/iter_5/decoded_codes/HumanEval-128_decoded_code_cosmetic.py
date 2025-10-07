from typing import Sequence, Optional, Union

def prod_sign(sequence_of_vals: Sequence[int]) -> Optional[int]:
    if not sequence_of_vals:
        return None

    if any(element == 0 for element in sequence_of_vals):
        product_sign = 0
    else:
        negative_elements_count = sum(1 for item in sequence_of_vals if item < 0)
        product_sign = (-1) ** negative_elements_count

    total_magnitude = sum(abs(sequence_of_vals[i]) for i in range(len(sequence_of_vals)))

    return product_sign * total_magnitude