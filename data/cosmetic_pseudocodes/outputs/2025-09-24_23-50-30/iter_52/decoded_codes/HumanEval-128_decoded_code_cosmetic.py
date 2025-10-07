from typing import List, Optional


def prod_sign(list_values: List[int]) -> Optional[int]:
    def compute_sign(idx: int, acc_neg_count: int) -> int:
        if idx == len(list_values):
            return 1 if acc_neg_count % 2 == 0 else -1
        return compute_sign(idx + 1, acc_neg_count + (1 if list_values[idx] < 0 else 0))

    if len(list_values) == 0:
        return None

    if 0 in list_values:
        tmp_sign = 0
    else:
        tmp_sign = compute_sign(0, 0)

    def sum_abs_values(i: int, acc_sum: int) -> int:
        if i == len(list_values):
            return acc_sum
        return sum_abs_values(i + 1, acc_sum + abs(list_values[i]))

    total_magnitude = sum_abs_values(0, 0)
    return tmp_sign * total_magnitude