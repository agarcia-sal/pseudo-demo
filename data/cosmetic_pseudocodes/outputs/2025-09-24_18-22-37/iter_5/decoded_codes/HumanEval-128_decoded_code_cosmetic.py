from typing import List, Optional

def prod_signs(list_of_numbers: List[int]) -> Optional[int]:
    if not list_of_numbers:
        return None

    if 0 in list_of_numbers:
        result_sign = 0
    else:
        neg_count = sum(1 for x in list_of_numbers if x < 0)
        result_sign = (-1) ** neg_count

    total_magnitude = sum(abs(x) for x in list_of_numbers)
    return result_sign * total_magnitude