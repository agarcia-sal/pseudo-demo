from typing import List, Optional

def prod_signs(list_of_numbers: List[int]) -> Optional[int]:
    if not list_of_numbers:
        return None
    if 0 in list_of_numbers:
        cumulative_sign = 0
    else:
        negatives_count = sum(1 for element in list_of_numbers if element < 0)
        cumulative_sign = (-1) ** negatives_count
    total_magnitude = sum(value if value >= 0 else -value for value in list_of_numbers)
    return cumulative_sign * total_magnitude