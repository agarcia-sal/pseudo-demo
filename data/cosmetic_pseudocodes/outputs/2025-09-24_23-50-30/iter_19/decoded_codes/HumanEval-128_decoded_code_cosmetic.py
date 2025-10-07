from functools import reduce
from typing import Sequence, Optional, Union

def prod_signs(sequence: Sequence[int]) -> Optional[int]:
    if not sequence:
        return None
    if 0 in sequence:
        result_sign = 0
    else:
        neg_count = sum(1 for x in sequence if x < 0)
        result_sign = 1 - 2 * (neg_count % 2)
    magnitude_total = reduce(
        lambda acc, y: acc + (y * (-1 if y < 0 else 1)),
        sequence,
        0,
    )
    return result_sign * magnitude_total