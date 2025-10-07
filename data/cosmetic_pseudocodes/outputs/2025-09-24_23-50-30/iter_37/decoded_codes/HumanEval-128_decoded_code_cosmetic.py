from typing import Optional, List

def prod_signs(list_of_vals: List[int]) -> Optional[int]:
    if len(list_of_vals) == 0:
        return None

    sign_flag: int = 1
    if any(val == 0 for val in list_of_vals):
        sign_flag = 0
    else:
        neg_count: int = sum(1 for elem in list_of_vals if elem < 0)
        sign_flag = (-1) ** neg_count

    sum_abs: int = 0
    index: int = 0
    while index < len(list_of_vals):
        x = list_of_vals[index]
        sum_abs += -x if x < 0 else x
        index += 1

    return sign_flag * sum_abs