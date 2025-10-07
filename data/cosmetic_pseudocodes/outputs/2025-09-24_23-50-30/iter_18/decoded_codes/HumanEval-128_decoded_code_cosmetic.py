from typing import List, Optional


def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if not list_of_values:
        return None

    sign_result: Optional[int] = None
    neg_count: int = 0

    for current_value in list_of_values:
        if current_value == 0:
            sign_result = 0
            break
        if current_value < 0:
            neg_count += 1

    if sign_result is None:
        power = 1
        for _ in range(neg_count):
            power *= -1
        sign_result = power

    abs_sum = 0
    idx = 0
    length = len(list_of_values)
    while idx < length:
        val = list_of_values[idx]
        abs_sum += val if val >= 0 else -val
        idx += 1

    return sign_result * abs_sum