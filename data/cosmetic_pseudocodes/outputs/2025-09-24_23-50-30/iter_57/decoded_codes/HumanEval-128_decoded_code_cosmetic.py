from typing import List, Optional


def prod_signs(list_of_nums: List[int]) -> Optional[int]:
    idx: int = 0
    has_zero: bool = False
    negatives_total: int = 0

    if not list_of_nums:
        return None

    while idx < len(list_of_nums):
        if not has_zero:
            if list_of_nums[idx] == 0:
                has_zero = True
            else:
                if list_of_nums[idx] < 0:
                    negatives_total += 1
        idx += 1

    product_sign: int = 0 if has_zero else (-1) ** negatives_total

    total_abs_sum: int = 0
    pos: int = 0

    while pos < len(list_of_nums):
        total_abs_sum += abs(list_of_nums[pos])
        pos += 1

    return product_sign * total_abs_sum