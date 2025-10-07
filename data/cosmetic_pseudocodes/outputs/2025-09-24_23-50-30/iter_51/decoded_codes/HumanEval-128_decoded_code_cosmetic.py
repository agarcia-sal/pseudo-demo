from typing import List, Optional


def prod_signs(input_list: List[int]) -> Optional[int]:
    if len(input_list) == 0:
        return None

    def check_zero(lst: List[int], idx: int) -> bool:
        if idx == len(lst):
            return False
        return lst[idx] == 0 or check_zero(lst, idx + 1)

    if check_zero(input_list, 0):
        result_sign = 0
    else:
        def neg_count(lst: List[int], pos: int, acc: int) -> int:
            if pos == len(lst):
                return acc
            return neg_count(lst, pos + 1, acc + (1 if lst[pos] < 0 else 0))

        negatives = neg_count(input_list, 0, 0)
        power_val = negatives
        result_sign = (-1) ** power_val

    def total_abs(lst: List[int], i: int, total: int) -> int:
        if i == len(lst):
            return total
        return total_abs(lst, i + 1, total + (-lst[i] if lst[i] < 0 else lst[i]))

    magnitude_sum = total_abs(input_list, 0, 0)
    return result_sign * magnitude_sum