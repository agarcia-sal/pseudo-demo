from typing import Sequence, Optional

def prod_signs(sequence: Sequence[int]) -> Optional[int]:
    if len(sequence) == 0:
        return None
    if 0 in sequence:
        result_sign = 0
    else:
        negative_tally = sum(1 for element in sequence if element < 0)
        result_sign = 1
        while negative_tally > 0:
            result_sign = -result_sign
            negative_tally -= 1
    magnitude_total = sum(value if value >= 0 else -value for value in sequence)
    return result_sign * magnitude_total