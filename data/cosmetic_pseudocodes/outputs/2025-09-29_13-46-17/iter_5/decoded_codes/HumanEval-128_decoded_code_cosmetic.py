from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def helper_calc(index: int, neg_count: int, zero_flag: bool, total_abs: int) -> int:
        if index == len(array_of_integers):
            if zero_flag:
                product_sign = 0
            else:
                product_sign = 1
                # Flip sign neg_count times
                product_sign = -1 if neg_count % 2 else 1
            return product_sign * total_abs
        current_val = array_of_integers[index]
        next_zero_flag = zero_flag or (current_val == 0)
        next_neg_count = neg_count + (1 if current_val < 0 else 0)
        next_total_abs = total_abs + (-current_val if current_val < 0 else current_val)
        return helper_calc(index + 1, next_neg_count, next_zero_flag, next_total_abs)

    if len(array_of_integers) == 0:
        return None
    return helper_calc(0, 0, False, 0)