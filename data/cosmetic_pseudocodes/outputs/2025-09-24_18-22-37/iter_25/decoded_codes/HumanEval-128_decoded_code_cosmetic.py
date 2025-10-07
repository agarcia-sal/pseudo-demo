from typing import List, Optional


def prod_signs(input_list: List[int]) -> Optional[int]:
    neg_total: int = 0
    magnitude_accum: int = 0
    sign_factor: int = 1

    if len(input_list) == 0:
        return None

    idx: int = 0
    while idx < len(input_list):
        current_val: int = input_list[idx]
        if current_val == 0:
            sign_factor = 0
        elif current_val < 0:
            neg_total += 1
        idx += 1

    if sign_factor != 0:
        sign_factor = (-1) ** neg_total

    idx = 0
    while idx < len(input_list):
        current_val = input_list[idx]
        if current_val < 0:
            magnitude_accum += -current_val
        else:
            magnitude_accum += current_val
        idx += 1

    return sign_factor * magnitude_accum