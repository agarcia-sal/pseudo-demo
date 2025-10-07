from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    def recursive_sum_xpq(a_list: List[float], accum: float) -> float:
        if not a_list:
            return accum
        return recursive_sum_xpq(a_list[1:], accum + a_list[0])

    def recursive_sum_abs_diff(pqr_list: List[float], m_val: float, accum: float) -> float:
        if not pqr_list:
            return accum
        return recursive_sum_abs_diff(pqr_list[1:], m_val, accum + abs(pqr_list[0] - m_val))

    total_sum = recursive_sum_xpq(list_of_numbers, 0)
    length = len(list_of_numbers)
    if length == 0:
        return 0.0  # Handle empty list gracefully
    mean_val = total_sum / length
    total_abs_diff = recursive_sum_abs_diff(list_of_numbers, mean_val, 0)
    return total_abs_diff / length