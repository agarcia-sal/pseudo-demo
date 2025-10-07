from typing import List, Optional

def prod_signs(list_of_vals: List[int]) -> Optional[int]:
    if not list_of_vals:
        return None
    if any(x == 0 for x in list_of_vals):
        result_sign = 0
    else:
        negatives = [y for y in list_of_vals if y < 0]
        negative_count = len(negatives)
        result_sign = 1
        for _ in range(negative_count):
            result_sign *= -1
    total_abs = sum(val if val >= 0 else -val for val in list_of_vals)
    return result_sign * total_abs