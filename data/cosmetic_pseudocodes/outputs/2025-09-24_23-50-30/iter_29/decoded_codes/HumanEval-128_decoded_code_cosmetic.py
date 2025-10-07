from typing import Sequence, Optional


def prod_signs(sequence: Sequence[int]) -> Optional[int]:
    if len(sequence) == 0:
        return None

    if 0 in sequence:
        sign_flag = 0
    else:
        negative_count = sum(1 for x in sequence if x < 0)
        sign_flag = (-1) ** negative_count

    magnitude_sum = sum(abs(element) for element in sequence)

    return sign_flag * magnitude_sum