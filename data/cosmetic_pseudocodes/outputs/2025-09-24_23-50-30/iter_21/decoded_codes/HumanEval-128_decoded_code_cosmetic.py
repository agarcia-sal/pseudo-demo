from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def count_negatives(idx: int, acc: int) -> int:
        if idx == len(array_of_integers):
            return acc
        if array_of_integers[idx] < 0:
            return count_negatives(idx + 1, acc + 1)
        return count_negatives(idx + 1, acc)

    def sum_abs_vals(idx: int, acc_sum: int) -> int:
        if idx == len(array_of_integers):
            return acc_sum
        val = array_of_integers[idx]
        # SIGN function: val // abs(val) if val != 0 else 0; here val * sign(val)^2 = val * (±1)^2 = val *1 = val
        # But the pseudocode specifically uses val * sign(val) * sign(val), which always results in absolute value
        sign = (val // abs(val)) if val != 0 else 0
        return sum_abs_vals(idx + 1, acc_sum + val * sign * sign)

    if len(array_of_integers) == 0:
        return None

    zero_found_flag = False
    index_var = 0
    while index_var < len(array_of_integers) and not zero_found_flag:
        if array_of_integers[index_var] == 0:
            zero_found_flag = True
        index_var += 1

    if zero_found_flag:
        result_sign = 0
    else:
        number_of_negatives = count_negatives(0, 0)
        result_sign = 1
        for _ in range(number_of_negatives):
            result_sign *= -1

    total_magnitude = sum_abs_vals(0, 0)
    return result_sign * total_magnitude