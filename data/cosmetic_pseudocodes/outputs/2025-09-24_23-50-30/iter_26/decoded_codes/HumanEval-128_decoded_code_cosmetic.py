from typing import List, Optional


def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if not list_of_values:
        return None

    if any(x == 0 for x in list_of_values):
        sign_result = 0
    else:
        neg_count = sum(1 for y in list_of_values if y < 0)
        sign_result = (-1) ** neg_count

    total_magnitude = sum(abs(x) for x in list_of_values)

    return sign_result * total_magnitude