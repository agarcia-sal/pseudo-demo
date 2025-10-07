from typing import List, Optional

def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if not list_of_values:
        return None
    if 0 in list_of_values:
        accumulated_sign = 0
    else:
        negatives_filtered = [element for element in list_of_values if element < 0]
        negatives_amount = 0
        for _ in negatives_filtered:
            negatives_amount += 1
        accumulated_sign = 1
        for _ in range(1, negatives_amount + 1):
            accumulated_sign *= -1
    total_abs = 0
    for value in list_of_values:
        total_abs += -value if value < 0 else value
    return accumulated_sign * total_abs