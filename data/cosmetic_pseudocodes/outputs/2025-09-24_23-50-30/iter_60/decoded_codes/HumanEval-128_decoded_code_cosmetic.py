from typing import List, Optional


def prod_signs(vecParam: List[int]) -> Optional[int]:
    index: int = 0
    result_sign: Optional[int] = None
    acc_magnitude: int = 0

    if len(vecParam) == 0:
        return result_sign

    def loop_check_zero(i: int) -> bool:
        if i >= len(vecParam):
            return False
        if vecParam[i] == 0:
            return True
        return loop_check_zero(i + 1)

    zero_present: bool = loop_check_zero(index)

    if zero_present:
        result_sign = 0
    else:
        def count_negatives(idx: int, neg_count: int) -> int:
            if idx >= len(vecParam):
                return neg_count
            if vecParam[idx] < 0:
                return count_negatives(idx + 1, neg_count + 1)
            return count_negatives(idx + 1, neg_count)

        negative_count: int = count_negatives(0, 0)

        def power(base: int, exp: int, accum: int) -> int:
            if exp <= 0:
                return accum
            return power(base, exp - 1, accum * base)

        result_sign = power(-1, negative_count, 1)

    def sum_abs_elements(pos: int, total: int) -> int:
        if pos >= len(vecParam):
            return total
        elem_abs: int = vecParam[pos] if vecParam[pos] >= 0 else -vecParam[pos]
        return sum_abs_elements(pos + 1, total + elem_abs)

    acc_magnitude = sum_abs_elements(0, 0)
    return result_sign * acc_magnitude