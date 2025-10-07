from typing import List, Optional


def prod_signs(lst_numbers: List[int]) -> Optional[int]:
    idx: int = 0
    flag_zero_found: bool = False
    length: int = len(lst_numbers)

    # Check for zero in the list
    while idx < length and not flag_zero_found:
        if lst_numbers[idx] == 0:
            flag_zero_found = True
        else:
            idx += 1

    if length == 0:
        return None

    if flag_zero_found:
        result_sign = 0
    else:
        neg_count = 0
        pos_idx = 0
        # Count negative numbers
        while pos_idx < length:
            if lst_numbers[pos_idx] < 0:
                neg_count += 1
            pos_idx += 1
        # Determine sign based on count of negatives
        result_sign = 1
        power_idx = 0
        while power_idx < neg_count:
            result_sign *= -1
            power_idx += 1

    total_abs_sum = 0
    j = 0
    # Sum absolute values of elements
    while j < length:
        val = lst_numbers[j]
        abs_val = -val if val < 0 else val
        total_abs_sum += abs_val
        j += 1

    return result_sign * total_abs_sum