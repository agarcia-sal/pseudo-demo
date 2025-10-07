from typing import List, Optional

def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if not list_of_values:
        return None
    if 0 in list_of_values:
        result_sign = 0
    else:
        negative_count = sum(1 for x in list_of_values if x < 0)
        result_sign = (-1) ** negative_count
    magnitude_sum = sum(abs(y) for y in list_of_values)
    return result_sign * magnitude_sum